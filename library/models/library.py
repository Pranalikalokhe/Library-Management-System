from utils.file_io import load_data, save_data
from utils.date_utils import calculate_late_fee
from models.book import Book
from models.member import Member
from datetime import datetime
from utils.decorators import log_action


class Library:
    def __init__(self):
        self.books = load_data('data/books.json')
        self.members = load_data('data/members.json')

    def save_all(self):
        save_data('data/books.json', self.books)
        save_data('data/members.json', self.members)
        
    @log_action
    def register_member(self):
        name = input("Enter member name: ").strip()
        member_id = input("Enter member ID: ").strip()
        if any(m['id'] == member_id for m in self.members):
            print("Member already exists.")
            return
        new_member = {
            "id": member_id,
            "name": name,
            "borrowed_books": []
        }
        self.members.append(new_member)
        self.save_all()
        print("Member registered successfully.")
        
        
    @log_action
    def add_book(self):
        isbn = input("Enter ISBN: ").strip()
        title = input("Enter title: ").strip()
        author = input("Enter author: ").strip()
        if any(b['isbn'] == isbn for b in self.books):
            print("Book already exists.")
            return
        new_book = {
            "isbn": isbn,
            "title": title,
            "author": author,
            "available": True
        }
        self.books.append(new_book)
        self.save_all()
        print("Book added.")

    def borrow_book(self):
        member_id = input("Enter member ID: ").strip()
        isbn = input("Enter book ISBN: ").strip()
        member = next((m for m in self.members if m['id'] == member_id), None)
        book = next((b for b in self.books if b['isbn'] == isbn), None)

        if not member:
            print("Member not found.")
            return
        if not book:
            print("Book not found.")
            return
        if not book.get('available', True):
            print("Book is currently borrowed.")
            return

        borrow_date = datetime.today().strftime('%Y-%m-%d')
        member['borrowed_books'].append({
            "isbn": isbn,
            "borrow_date": borrow_date
        })
        book['available'] = False
        self.save_all()
        print(f"Book borrowed on {borrow_date}.")

    def return_book(self):
        member_id = input("Enter member ID: ").strip()
        isbn = input("Enter book ISBN: ").strip()
        member = next((m for m in self.members if m['id'] == member_id), None)
        book = next((b for b in self.books if b['isbn'] == isbn), None)

        if not member or not book:
            print("Member or Book not found.")
            return

        borrowed = next((b for b in member['borrowed_books'] if b['isbn'] == isbn), None)
        if not borrowed:
            print("This book is not borrowed by the member.")
            return

        fee = calculate_late_fee(borrowed['borrow_date'])

        member['borrowed_books'].remove(borrowed)
        book['available'] = True
        self.save_all()

        print(f"Book returned successfully. Late fee: ₹{fee}")

    def view_member_history(self):
        member_id = input("Enter member ID: ").strip()
        member = next((m for m in self.members if m['id'] == member_id), None)

        if not member:
            print("Member not found.")
            return

        if not member['borrowed_books']:
            print("No borrowed books.")
        else:
            print(f"Borrowed books for {member['name']}:")
            for book in member['borrowed_books']:
                print(f" - ISBN: {book['isbn']}, Borrow Date: {book['borrow_date']}")

    def get_overdue_books(self):
        for member in self.members:
            for borrowed in member.get('borrowed_books', []):
                borrow_date = borrowed.get("borrow_date")
                if borrow_date:
                    fee = calculate_late_fee(borrow_date)
                    if fee > 0:
                        yield {
                            "member": member['name'],
                            "book_id": borrowed["isbn"],
                            "borrow_date": borrow_date,
                            "late_fee": fee
                        }
