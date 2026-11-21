# Planning Utilities

## Marketing budget allocator

`budget_allocator.py` distributes an integer budget proportionally across named workstreams.

### Requirements

- Python 3.9 or newer
- No third-party dependencies

### Example

The utility accepts integer minor currency units (such as cents) to avoid floating-point currency rounding.

```bash
python tools/budget_allocator.py --total 100000 --weights '{"brand": 30, "education": 20, "demand": 50}'
```

The resulting allocations always sum to the requested total. If rounding leaves a remainder, the utility distributes it by largest fractional remainder, with alphabetical tie-breaking for reproducible output.

### Run tests

From the repository root:

```bash
python -m unittest discover -s tests -v
```

### Limitations

- Weights express relative proportions; they are not ROI forecasts.
- The utility does not recommend budget shares or optimize for performance.
- Human review is required before using allocations in a real budget.
