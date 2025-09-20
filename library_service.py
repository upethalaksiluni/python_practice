from datetime import datetime

from Day9.library_system.models import Book, Member, Loan
from Day9.library_system.repositories import BookRepository, MemberRepository, LoanRepository


class LibraryException(Exception):
    pass


class LibraryService:
    books: BookRepository
    members: MemberRepository
    loans: LoanRepository

    # def __init__(self, books: BookRepository, members:MemberRepository, loans:LoanRepository):
    #     self.books = books
    #     self.members = members
    #     self.loans = loans

    def add_books(self, book_id: str, title: str, author: str, year: str) -> Book:
        if self.books.get_by_id(book_id) is not None:
            raise LibraryException("Book already exists")

        book = Book(book_id, title, author, year)

        self.books.add_book(book)
        return book

    def add_member(self, member_id: str, name: str) -> Member:
        if self.members.get_member_by_id(member_id) is not None:
            raise LibraryException("Member already exists")

        member = Member(member_id, name)

        self.members.add(member)
        return member

    def borrow_book(self, loan_id: str, member_id: str, book_id: str):
        if self.books.get_by_id(book_id) is None:
            raise LibraryException("Book doesn't exist")

        if self.members.get_member_by_id(member_id) is None:
            raise LibraryException("Member does not exist")

        if not self.books.get_by_id(book_id).is_available():
            raise LibraryException("Book is already borrowed")

        loan = Loan(loan_id, member_id, book_id, datetime.now())
        self.loans.add_Loan(loan)
        book = self.books.get_by_id(book_id)
        book.book_lend_member_id = member_id

        self.books.update(book)

    def return_book(self, loan_id: str, member_id: str, book_id: str) -> Book:
        loan = self.loans.get_by_id(loan_id)
        if loan is None or not loan.is_active():
            raise LibraryException("Loan not found or already returned")

        if loan.member_id != member_id or loan.book_id != book_id:
            raise LibraryException("Loan details do not match")

        loan.returned_at = datetime.now()
        self.loans.update(loan)

        book = self.books.get_by_id(book_id)
        book.book_lend_member_id = None
        self.books.update(book)

        return book


