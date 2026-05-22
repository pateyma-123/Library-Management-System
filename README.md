# Library Management System

A comprehensive Python-based library management system that allows users to manage books, members, and book loans efficiently.

## 📋 Features

The system provides the following functionality:

1. **Add Book** - Register new books in the library with ID, title, and author
2. **Register Member** - Add new members with ID, name, and email
3. **Borrow Book** - Create a loan for a member to borrow a book
4. **Return Book** - Process book returns and close loans
5. **View Books** - Display all books with their availability status
6. **View Members** - List all registered members
7. **View Loans** - Display all active and closed loans
8. **Exit** - Gracefully close the program

## 📁 Project Structure

```
Library-Management-System/
├── book.py              # Book class definition
├── member.py            # Member class definition
├── loan.py              # Loan class definition
├── exceptions.py        # Custom exception classes
├── library_service.py   # Core service managing all operations
├── main.py              # CLI interface
└── README.md            # Project documentation
```

## 🏗️ Architecture

### Classes

#### **Book**
Represents a book in the library.
- `book_id`: Unique identifier
- `title`: Book title
- `author`: Author name
- `available`: Boolean flag indicating availability status
- Methods: `borrow()`, `return_book()`

#### **Member**
Represents a library member.
- `member_id`: Unique identifier
- `name`: Member's name
- `email`: Member's email address

#### **Loan**
Represents a book loan transaction.
- `loan_id`: Unique identifier (format: L001, L002, etc.)
- `book`: Reference to borrowed book
- `member`: Reference to borrowing member
- `borrow_date`: Timestamp when book was borrowed
- `return_date`: Timestamp when book was returned
- `is_active`: Boolean indicating if loan is still active
- Methods: `close_loan()`

#### **LibraryService**
Core service managing all library operations.
- Methods:
  - `add_book(book_id, title, author)`
  - `view_books()`
  - `register_member(member_id, name, email)`
  - `view_members()`
  - `borrow_book(book_id, member_id)`
  - `return_book(loan_id)`
  - `view_loans()`

### Exceptions

- `BookNotFoundError` - Raised when a book is not found
- `MemberNotFoundError` - Raised when a member is not found
- `BookUnavailableError` - Raised when a book is already borrowed
- `LoanNotFoundError` - Raised when a loan is not found

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher

### Installation

1. Clone the repository:
```bash
git clone https://github.com/pateyma-123/Library-Management-System.git
cd Library-Management-System
```

2. Run the program:
```bash
python main.py
```

## 💻 Usage

After running `python main.py`, you'll see an interactive menu:

```
==================================================
LIBRARY MANAGEMENT SYSTEM
==================================================
1. Add Book
2. Register Member
3. Borrow Book
4. Return Book
5. View Books
6. View Members
7. View Loans
8. Exit
==================================================
```

### Example Workflow

1. **Add a Book**
   - Choose option 1
   - Enter Book ID: `B001`
   - Enter Title: `Python Programming`
   - Enter Author: `Guido van Rossum`

2. **Register a Member**
   - Choose option 2
   - Enter Member ID: `M001`
   - Enter Name: `John Doe`
   - Enter Email: `john@example.com`

3. **Borrow a Book**
   - Choose option 3
   - Enter Book ID: `B001`
   - Enter Member ID: `M001`
   - Loan ID will be generated: `L001`

4. **View Books**
   - Choose option 5
   - See all books with their availability status

5. **Return a Book**
   - Choose option 4
   - Enter Loan ID: `L001`

6. **View All Loans**
   - Choose option 7
   - See active and closed loans

## 📊 Data Flow

### Borrow Book Flow
```
User Input (Book ID, Member ID)
    ↓
Lookup Book
    ↓
Lookup Member
    ↓
Check Book Availability
    ↓
Mark Book as Borrowed
    ↓
Create Loan Record
    ↓
Display Success Message
```

### Return Book Flow
```
User Input (Loan ID)
    ↓
Find Loan Record
    ↓
Mark Book as Available
    ↓
Close Loan Record
    ↓
Display Success Message
```

## ✨ Key Features

- **Unique Identification**: Each book, member, and loan has a unique ID
- **Availability Tracking**: System tracks which books are available vs. borrowed
- **Error Handling**: Comprehensive error handling with custom exceptions
- **Input Validation**: All user inputs are validated before processing
- **Transaction History**: All loans are recorded with timestamps

## 🔒 Error Handling

The system gracefully handles errors:

- **Book not found** - When trying to borrow/access a non-existent book
- **Member not found** - When trying to borrow with a non-existent member
- **Book unavailable** - When trying to borrow an already borrowed book
- **Loan not found** - When trying to return with an invalid loan ID
- **Invalid input** - When user provides empty or invalid data

## 📝 Example Output

```
✓ Book added: Python Programming

✓ Member registered: John Doe

✓ John Doe borrowed Python Programming
  Loan ID: L001

Books:
------------------------------------------------------------
B001 - Python Programming by Guido van Rossum [Borrowed]
------------------------------------------------------------

Members:
------------------------------------------------------------
M001 - John Doe (john@example.com)
------------------------------------------------------------

Loans:
--------------------------------------------------------------------------------
L001 - John Doe borrowed Python Programming [Active]
--------------------------------------------------------------------------------
```

## 🎯 Future Enhancements

- Data persistence (save to database)
- Due date tracking for loans
- Fine calculation for overdue books
- Book rating and reviews
- Advanced search functionality
- Web-based interface

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

Created for the Library Management System mini project.

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests.

---

**Happy Library Managing! 📚**
