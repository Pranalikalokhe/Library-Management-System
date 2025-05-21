import unittest
from unittest.mock import patch, MagicMock
from library.models.library import Library

class LibraryTestCase(unittest.TestCase):
    def setUp(self):
        # Set up a mock library with sample data
        self.library = Library()
        self.library.books = [
            {"isbn": "123", "title": "Test Book", "author": "Author A", "available": True}
        ]
        self.library.members = [
            {"id": "M001", "name": "Alice", "role": "member", "borrowed_books": []},
            {"id": "A001", "name": "Admin", "role": "admin", "borrowed_books": []}
        ]

    @patch("builtins.input", side_effect=["M001"])
    def test_login_successful(self, mock_input):
        member = self.library.login()
        self.assertIsNotNone(member)
        self.assertEqual(member['id'], "M001")

    @patch("builtins.input", side_effect=["M999"])
    def test_login_failure(self, mock_input):
        member = self.library.login()
        self.assertIsNone(member)

    @patch("builtins.input", side_effect=["Alice", "M002", "member"])
    def test_register_member(self, mock_input):
        self.library.register_member()
        self.assertTrue(any(m['id'] == "M002" for m in self.library.members))

    @patch("builtins.input", side_effect=["A001", "456", "New Book", "Author B"])
    def test_add_book_as_admin(self, mock_input):
        self.library.add_book()
        self.assertTrue(any(b['isbn'] == "456" for b in self.library.books))

    @patch("builtins.input", side_effect=["M001", "123"])
    def test_borrow_book(self, mock_input):
        self.library.borrow_book()
        member = next(m for m in self.library.members if m['id'] == "M001")
        book = next(b for b in self.library.books if b['isbn'] == "123")
        self.assertFalse(book['available'])
        self.assertEqual(len(member['borrowed_books']), 1)

    @patch("builtins.input", side_effect=["M001", "123"])
    def test_return_book(self, mock_input):
        # Simulate borrowing
        self.library.members[0]["borrowed_books"].append({
            "isbn": "123",
            "borrow_date": "2024-05-01"
        })
        self.library.books[0]["available"] = False
        self.library.return_book()
        member = self.library.members[0]
        book = self.library.books[0]
        self.assertTrue(book["available"])
        self.assertEqual(len(member["borrowed_books"]), 0)

    @patch("builtins.input", side_effect=["M001"])
    def test_view_member_history(self, mock_input):
        self.library.members[0]["borrowed_books"].append({
            "isbn": "123",
            "borrow_date": "2024-05-01"
        })
        with patch("builtins.print") as mock_print:
            self.library.view_member_history()
            mock_print.assert_any_call("Borrowed books for Alice:")

    def test_get_overdue_books(self):
        self.library.members[0]["borrowed_books"].append({
            "isbn": "123",
            "borrow_date": "2024-01-01"
        })
        overdue = list(self.library.get_overdue_books())
        self.assertGreater(overdue[0]["late_fee"], 0)

if __name__ == "__main__":
    unittest.main()
