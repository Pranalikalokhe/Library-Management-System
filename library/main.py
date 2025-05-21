from models.library import Library

def main():
    lib = Library()
    
    while True:
        print("\n--- Library Management System ---")
        print("1. Register Member")
        print("2. Add Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View Member History")
        print("6.  Overdue Books ")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            lib.register_member()
        elif choice == '2':
            lib.add_book()
        elif choice == '3':
            lib.borrow_book()
        elif choice == '4':
            lib.return_book()
        elif choice == '5':
            lib.view_member_history()
        elif choice == '6':
            print("\n--- Overdue Books ---")
            for record in lib.get_overdue_books():
             print(f"{record['member']} has overdue book ID {record['book_id']} (Borrowed on {record['borrow_date']}) - Fee: ₹{record['late_fee']}")
    
        elif choice == '7':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            

if __name__ == "__main__":
    main()
