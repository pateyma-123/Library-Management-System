class LibraryException(Exception):
    """Base exception for library operations."""
    pass


class BookNotFoundError(LibraryException):
    """Raised when a book is not found in the library."""
    pass


class MemberNotFoundError(LibraryException):
    """Raised when a member is not found in the library."""
    pass


class BookUnavailableError(LibraryException):
    """Raised when a book is already borrowed."""
    pass


class LoanNotFoundError(LibraryException):
    """Raised when a loan is not found."""
    pass
