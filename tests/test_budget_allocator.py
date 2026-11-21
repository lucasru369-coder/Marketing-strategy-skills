"""Unit tests for the marketing budget allocator."""

import unittest

from tools.budget_allocator import allocate_budget


class AllocateBudgetTests(unittest.TestCase):
    def test_preserves_total_with_even_split(self):
        self.assertEqual(
            allocate_budget(100, {"brand": 1, "demand": 1}),
            {"brand": 50, "demand": 50},
        )

    def test_preserves_total_with_rounding_remainder(self):
        result = allocate_budget(100, {"alpha": 1, "beta": 1, "gamma": 1})
        self.assertEqual(sum(result.values()), 100)
        self.assertEqual(result, {"alpha": 34, "beta": 33, "gamma": 33})

    def test_zero_weight_category_receives_zero(self):
        result = allocate_budget(250, {"research": 0, "media": 5})
        self.assertEqual(result, {"research": 0, "media": 250})

    def test_zero_total_is_valid(self):
        self.assertEqual(allocate_budget(0, {"brand": 3}), {"brand": 0})

    def test_rejects_negative_total(self):
        with self.assertRaises(ValueError):
            allocate_budget(-1, {"brand": 1})

    def test_rejects_non_integer_total(self):
        with self.assertRaises(TypeError):
            allocate_budget(10.5, {"brand": 1})

    def test_rejects_empty_weights(self):
        with self.assertRaises(ValueError):
            allocate_budget(100, {})

    def test_rejects_all_zero_weights(self):
        with self.assertRaises(ValueError):
            allocate_budget(100, {"brand": 0, "demand": 0})

    def test_rejects_negative_weight(self):
        with self.assertRaises(ValueError):
            allocate_budget(100, {"brand": -1, "demand": 2})

    def test_rejects_invalid_category_name(self):
        with self.assertRaises(ValueError):
            allocate_budget(100, {" ": 1})

    def test_rejects_non_numeric_weight(self):
        with self.assertRaises(TypeError):
            allocate_budget(100, {"brand": "high"})


if __name__ == "__main__":
    unittest.main()
