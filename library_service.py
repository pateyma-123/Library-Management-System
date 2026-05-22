from book import Book
from member import Member
from loan import Loan
from exceptions import (
    BookNotFoundError,
    MemberNotFoundError,
    BookUnavailableError,
    LoanNotFoundError
)


class LibraryService:
    """Service class for managing library operations."""
    
    def __init__(self):
        """Initialize the library service with empty collections."""
        self._books = {}
        self._members = {}
        self._loans = []
        self._loan_counter = 0
    
    # ========== BOOK OPERATIONS ==========
    
    def add_book(self, book_id, title, author):
        """
        Add a new book to the library.
        Flowchart: _01_add_book.svg
        
        Args:
            book_id (str): Unique identifier for the book
            title (str): Title of the book
            author (str): Author of the book
        
        Returns:
            Book: The created book object
        """
        book = Book(book_id, title, author)
        self._books[book_id] = book
        return book
    
    def view_books(self):
        """
        Get a list of all books in the library.
        Flowchart: _05_view_book.svg
        
        Returns:
            list: List of Book objects
        """
        return list(self._books.values())
    
    # ========== MEMBER OPERATIONS ==========
    
    def register_member(self, member_id, name, email):
        """
        Register a new member in the library.
        Flowchart: _02_register_member.svg
        
        Args:
            member_id (str): Unique identifier for the member
            name (str): Name of the member
            email (str): Email address of the member
        
        Returns:
            Member: The created member object
        """
        member = Member(member_id, name, email)
        self._members[member_id] = member
        return member
    
    def view_members(self):
        """
        Get a list of all members in the library.
        Flowchart: _06_view_member.svg
        
        Returns:
            list: List of Member objects
        """
        return list(self._members.values())
    
    # ========== LOAN OPERATIONS ==========
    
    def borrow_book(self, book_id, member_id):
        """
        Create a loan for a book.
        Flowchart: _03_borrow_book.svg
        
        Args:
            book_id (str): ID of the book to borrow
            member_id (str): ID of the member borrowing
        
        Returns:
            Loan: The created loan object
        
        Raises:
            BookNotFoundError: If book not found
            MemberNotFoundError: If member not found
            BookUnavailableError: If book is already borrowed
        """
        # Lookup book
        book = self._books.get(book_id)
        if book is None:
            raise BookNotFoundError("Book not found.")
        
        # Lookup member
        member = self._members.get(member_id)
        if member is None:
            raise MemberNotFoundError("Member not found.")
        
        # Check availability
        if not book.available:
            raise BookUnavailableError("Book is already borrowed.")
        
        # Mark book as borrowed
        book.borrow()
        
        # Create loan
        self._loan_counter += 1
        loan_id = f"L{self._loan_counter:03d}"
        loan = Loan(loan_id, book, member)
        self._loans.append(loan)
        
        return loan
    
    def return_book(self, loan_id):
        """
        Process the return of a borrowed book.
        Flowchart: _04_return_book.svg
        
        Args:
            loan_id (str): ID of the loan to close
        
        Returns:
            Loan: The closed loan object
        
        Raises:
            LoanNotFoundError: If loan not found
        """
        # Find the loan
        loan = None
        for l in self._loans:
            if l.loan_id == loan_id:
                loan = l
                break
        
        if loan is None:
            raise LoanNotFoundError(f"Loan {loan_id} not found.")
        
        # Mark book as available
        loan.book.return_book()
        
        # Close the loan
        loan.close_loan()
        
        return loan
    
    def view_loans(self):
        """
        Get a list of all loans in the library.
        Flowchart: _07_view_loan.svg
        
        Returns:
            list: List of Loan objects
        """
        return list(self._loans)
