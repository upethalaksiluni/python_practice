from abc import ABC, abstractmethod
from typing import List, Dict

from library_system.models import Book, Member, Loan


class BookRepository(ABC):

    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def get_by_id(self, book_id) -> Book:
        pass

    @abstractmethod
    def update(self, book: Book) -> None:
        pass

    @abstractmethod
    def list_all_books(self) -> List[Book]:
        pass


class MemberRepository(ABC):

    @abstractmethod
    def add(self, member: Member) -> None:
        pass

    @abstractmethod
    def get_member_by_id(self, member_id) -> Member:
        pass

    @abstractmethod
    def list_all_members(self) -> List[Member]:
        pass


class LoanRepository(ABC):

    @abstractmethod
    def add_Loan(self, loan: Loan) -> None:
        pass

    @abstractmethod
    def get_by_id(self, loan_id) -> Loan:
        pass

    @abstractmethod
    def update(self, loan: Loan) -> None:
        pass

    @abstractmethod
    def list_all_loans(self) -> List[Loan]:
        pass


class InMemoryBookRepository(BookRepository):

    def __init__(self):
        self.__books: Dict[str, Book] = {}

    def add_book(self, book: Book) -> None:
        self.__books[book.book_id] = book

    def get_by_id(self, book_id) -> Book:
        return self.__books.get(book_id)

    def update(self, book: Book) -> None:
        self.__books[book.book_id] = book

    def list_all_books(self) -> List[Book]:
        return list(self.__books.values())


class InMemoryMemberRepository(MemberRepository):

    def __init__(self):
        self.__members: Dict[str, Member] = {}

    def add(self, member: Member) -> None:
        self.__members[member.member_id] = member

    def get_member_by_id(self, member_id) -> Member:
        return self.__members.get(member_id)

    def list_all_members(self) -> List[Member]:
        return list(self.__members.values())


class InMemoryLoanRepository(LoanRepository):

    def __init__(self):
        self.__loans: Dict[str, Loan] = {}

    def add_Loan(self, loan: Loan) -> None:
        self.__loans[loan.loan_id] = loan

    def get_by_id(self, loan_id) -> Loan:
        return self.__loans.get(loan_id)

    def update(self, loan: Loan) -> None:
        self.__loans[loan.loan_id] = loan

    def list_all_loans(self) -> List[Loan]:
        return list(self.__loans.values())


class FileSaveBookRepository(BookRepository):

    def __init__(self, filename: str = "data/book.txt"):
        self.filename = filename

    def __save_books(self, books: Dict[str, Book]):
        with open(self.filename, 'w') as data:
            for key, book in books.items():
                data.write(f"{key} | {book.title} | {book.author} | {book.book_lend_member_id}\n")

    def __load_books(self) -> Dict[str, Book]:
        books: Dict[str, Book] = {}
        with open(self.filename, 'r') as book_file:
            for book in book_file:
                book = book.strip()
                data = book.split(sep="|")
                if len(data) == 5:
                    book_id, title, author, year, book_lend_member_id = data
                    books[book_id] = Book(
                        book_id=book_id,
                        author=author,
                        title=title,
                        year=year,
                        book_lend_member_id=book_lend_member_id if "None" not in book_lend_member_id else None
                    )
        return books

    def add_books(self, book: Book) -> None:
        books: Dict[str, Book] = self.load_books()
        books[book.book_id] = book
        self.save_books(books)

    def get_by_id(self, book_id) -> Book:
        books = self.load_books()
        return books.get(book_id)

    def update(self, book: Book) -> None:
        books: Dict[str, Book] = self.load_books()
        books[book.book_id] = book
        self.save_books(books)

    def list_all_books(self) -> List[Book]:
        return list(self.load_books().values())


class FileSaveMemberRepository(MemberRepository):

    def __init__(self, filename: str = "data/member.txt"):
        self.filename = filename

    def __save_members(self, members: Dict[str, Member]):
        with open(self.filename, 'w') as data:
            for key, member in members.items():
                data.write(f"{key} | {member.name}\n")

    def __load_members(self) -> Dict[str, Member]:
        members: Dict[str, Member] = {}
        with open(self.filename, 'r') as member_file:
            for member in member_file:
                member = member.strip()
                data = member.split(sep="|")
                if len(data) == 5:
                    member_id, name = data
                    members[member_id] = Member(
                        member_id=member_id,
                        name=name
                    )
        return members

    def add_members(self, member: Member) -> None:
        members: Dict[str, Member] = self.member_books()
        members[member.member_id] = member
        self.save_members(members)

    def get_by_id(self, member_id) -> Member:
        members = self.load_members()
        return members.get(member_id)

    def update(self, member: Member) -> None:
        members: Dict[str, Member] = self.load_members()
        members[member.member_id] = member
        self.save_books(members)

    def list_all_members(self) -> List[Member]:
        return list(self.load_members().values())
