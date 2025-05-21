import unittest
from utils.date_utils import calculate_late_fee # type: ignore

class TestLibraryFunctions(unittest.TestCase):

    def test_calculate_late_fee_no_fee(self):
        self.assertEqual(calculate_late_fee("2025-05-10"), 0)

    def test_calculate_late_fee_with_fee(self):
        self.assertGreaterEqual(calculate_late_fee("2025-04-01"), 1)

    def test_invalid_date(self):
        self.assertEqual(calculate_late_fee("invalid-date"), 0)

if __name__ == '__main__':
    unittest.main()
