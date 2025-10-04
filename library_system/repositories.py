from abc import ABC, abstractmethod
from typing import List, Dict

from library_system.models import Book, Member, Loan


class BookRepository(ABC):

    @abstractmethod
    def add_book(self, book : Book) -> None:
        pass

    @abstractmethod
    def get_by_id(self, book_id) -> Book:
        pass

    @abstractmethod
    def update(self, book : Book) -> None:
        pass

    @abstractmethod
    def list_all_books(self) -> List[Book]:
        pass


class MemberRepository(ABC):

    @abstractmethod
    def add(self, member : Member) -> None:
        pass

    @abstractmethod
    def get_member_by_id(self, member_id) -> Member:
        pass

    @abstractmethod
    def list_all_members(self) -> List[Member]:
        pass

class LoanRepository(ABC):

    @abstractmethod
    def add_Loan(self, loan : Loan) -> None:
        pass

    @abstractmethod
    def get_by_id(self, loan_id) -> Loan:
        pass

    @abstractmethod
    def update(self, loan : Loan) -> None:
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
