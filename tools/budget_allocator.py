"""Allocate a total marketing budget across weighted workstreams.

The utility uses only the Python standard library. Amounts are represented in
integer minor units (for example, cents) to avoid floating-point rounding drift.
"""

from __future__ import annotations

import argparse
import json
from typing import Mapping


def allocate_budget(total: int, weights: Mapping[str, float]) -> dict[str, int]:
    """Allocate an integer total proportionally and preserve the exact total.

    Any rounding remainder is assigned by descending fractional remainder;
    ties are resolved alphabetically for deterministic results.
    """
    if isinstance(total, bool) or not isinstance(total, int):
        raise TypeError("total must be an integer in minor currency units")
    if total < 0:
        raise ValueError("total must be zero or greater")
    if not weights:
        raise ValueError("at least one allocation category is required")

    normalized: dict[str, float] = {}
    for name, weight in weights.items():
        if not isinstance(name, str) or not name.strip():
            raise ValueError("category names must be non-empty strings")
        if isinstance(weight, bool) or not isinstance(weight, (int, float)):
            raise TypeError(f"weight for {name!r} must be numeric")
        if weight < 0:
            raise ValueError(f"weight for {name!r} must be zero or greater")
        normalized[name] = float(weight)

    weight_sum = sum(normalized.values())
    if weight_sum <= 0:
        raise ValueError("the sum of weights must be greater than zero")

    exact = {
        name: total * weight / weight_sum
        for name, weight in normalized.items()
    }
    result = {name: int(value) for name, value in exact.items()}
    remainder = total - sum(result.values())

    order = sorted(
        normalized,
        key=lambda name: (-(exact[name] - result[name]), name),
    )
    for name in order[:remainder]:
        result[name] += 1

    return result


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Allocate a marketing budget by proportional weights."
    )
    parser.add_argument(
        "--total",
        type=int,
        required=True,
        help="Total budget in integer minor units (for example, cents).",
    )
    parser.add_argument(
        "--weights",
        required=True,
        help='JSON object, for example: {"brand": 30, "demand": 70}',
    )
    args = parser.parse_args()

    try:
        weights = json.loads(args.weights)
        if not isinstance(weights, dict):
            raise ValueError("--weights must decode to a JSON object")
        allocation = allocate_budget(args.total, weights)
    except (json.JSONDecodeError, TypeError, ValueError) as error:
        parser.error(str(error))

    print(json.dumps(allocation, indent=2, sort_keys=True))
    print(f"Total allocated: {sum(allocation.values())}")


if __name__ == "__main__":
    main()
