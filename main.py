from library_service import LibraryService
from exceptions import (
    BookNotFoundError,
    MemberNotFoundError,
    BookUnavailableError,
    LoanNotFoundError
)


def display_menu():
    """Display the main menu."""
    print("\n" + "="*50)
    print("LIBRARY MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. View Books")
    print("6. View Members")
    print("7. View Loans")
    print("8. Exit")
    print("="*50)


def add_book(service):
    """Handle adding a new book."""
    try:
        book_id = input("Enter Book ID: ").strip()
        if not book_id:
            print("Error: Book ID cannot be empty.")
            return
        
        title = input("Enter Book Title: ").strip()
        if not title:
            print("Error: Title cannot be empty.")
            return
        
        author = input("Enter Book Author: ").strip()
        if not author:
            print("Error: Author cannot be empty.")
            return
        
        book = service.add_book(book_id, title, author)
        print(f"\n✓ Book added: {title}")
    except Exception as e:
        print(f"Error adding book: {e}")


def register_member(service):
    """Handle registering a new member."""
    try:
        member_id = input("Enter Member ID: ").strip()
        if not member_id:
            print("Error: Member ID cannot be empty.")
            return
        
        name = input("Enter Member Name: ").strip()
        if not name:
            print("Error: Name cannot be empty.")
            return
        
        email = input("Enter Member Email: ").strip()
        if not email:
            print("Error: Email cannot be empty.")
            return
        
        member = service.register_member(member_id, name, email)
        print(f"\n✓ Member registered: {name}")
    except Exception as e:
        print(f"Error registering member: {e}")


def borrow_book(service):
    """Handle borrowing a book."""
    try:
        book_id = input("Enter Book ID: ").strip()
        member_id = input("Enter Member ID: ").strip()
        
        if not book_id or not member_id:
            print("Error: Book ID and Member ID cannot be empty.")
            return
        
        loan = service.borrow_book(book_id, member_id)
        print(f"\n✓ {loan.member.name} borrowed {loan.book.title}")
        print(f"  Loan ID: {loan.loan_id}")
    except BookNotFoundError:
        print("Error: Book not found.")
    except MemberNotFoundError:
        print("Error: Member not found.")
    except BookUnavailableError:
        print("Error: Book is already borrowed.")
    except Exception as e:
        print(f"Error: {e}")


def return_book(service):
    """Handle returning a book."""
    try:
        loan_id = input("Enter Loan ID: ").strip()
        if not loan_id:
            print("Error: Loan ID cannot be empty.")
            return
        
        loan = service.return_book(loan_id)
        print(f"\n✓ {loan.member.name} returned {loan.book.title}")
        print(f"  Loan ID: {loan.loan_id}")
    except LoanNotFoundError:
        print("Error: Loan not found.")
    except Exception as e:
        print(f"Error: {e}")


def view_books(service):
    """Display all books in the library."""
    books = service.view_books()
    
    if not books:
        print("\nNo books found.")
        return
    
    print("\nBooks:")
    print("-" * 60)
    for book in books:
        print(book)
    print("-" * 60)


def view_members(service):
    """Display all members in the library."""
    members = service.view_members()
    
    if not members:
        print("\nNo members found.")
        return
    
    print("\nMembers:")
    print("-" * 60)
    for member in members:
        print(member)
    print("-" * 60)


def view_loans(service):
    """Display all loans in the library."""
    loans = service.view_loans()
    
    if not loans:
        print("\nNo loans found.")
        return
    
    print("\nLoans:")
    print("-" * 80)
    for loan in loans:
        print(loan)
    print("-" * 80)


def main():
    """Main program loop."""
    service = LibraryService()
    
    print("\nWelcome to Library Management System!")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ").strip()
        
        if choice == "1":
            add_book(service)
        elif choice == "2":
            register_member(service)
        elif choice == "3":
            borrow_book(service)
        elif choice == "4":
            return_book(service)
        elif choice == "5":
            view_books(service)
        elif choice == "6":
            view_members(service)
        elif choice == "7":
            view_loans(service)
        elif choice == "8":
            print("\nProgram closed.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
