"""Command-line tests for the marketing budget allocator."""

import json
import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "tools" / "budget_allocator.py"


class BudgetAllocatorCliTests(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            capture_output=True,
            text=True,
            check=False,
        )

    def test_cli_prints_allocation_and_total(self):
        result = self.run_cli(
            "--total", "1000",
            "--weights", '{"brand": 25, "demand": 75}',
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        lines = result.stdout.strip().splitlines()
        allocation = json.loads("\n".join(lines[:-1]))
        self.assertEqual(allocation, {"brand": 250, "demand": 750})
        self.assertIn("Total allocated: 1000", lines[-1])

    def test_cli_rejects_invalid_json(self):
        result = self.run_cli("--total", "100", "--weights", "{invalid")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("usage:", result.stderr.lower())

    def test_cli_rejects_non_object_json(self):
        result = self.run_cli("--total", "100", "--weights", "[1, 2]")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("JSON object", result.stderr)


if __name__ == "__main__":
    unittest.main()
