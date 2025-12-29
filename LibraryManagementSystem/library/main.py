#from models.library import Library
from library.models.library import Library



def main():
    lib = Library()
    user = lib.login()
    if not user:
        return

    while True:
        print("\n--- Library Management System ---")
        print("1. Register Member (admin only)")
        print("2. Add Book (admin only)")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View Member History")
        print("6. Overdue Books")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            if user['role'] == 'admin':
                lib.register_member()
            else:
                print("Permission denied. Only admins can register members.")

        elif choice == '2':
            if user['role'] == 'admin':
                lib.add_book()
            else:
                print("Permission denied. Only admins can add books.")

        elif choice == '3':
            if user['role'] == 'member':
                lib.borrow_book()
            else:
                print("Only members can borrow books.")

        elif choice == '4':
            if user['role'] == 'member':
                lib.return_book()
            else:
                print("Only members can return books.")

        elif choice == '5':
            lib.view_member_history()

        elif choice == '6':
            for record in lib.get_overdue_books():
                print(f"{record['member']} has overdue book ID {record['book_id']} (Borrowed on {record['borrow_date']}) - Fee: ₹{record['late_fee']}")

        elif choice == '7':
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()            
