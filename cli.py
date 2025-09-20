from library_service import LibraryService, LibraryException
from repositories import InMemoryBookRepository, InMemoryMemberRepository, InMemoryLoanRepository


def main():
    book_repo = InMemoryBookRepository()
    member_repo = InMemoryMemberRepository()
    loan_repo = InMemoryLoanRepository()

    service = LibraryService()
    service.books = book_repo
    service.members = member_repo
    service.loans = loan_repo

    try:
        print("Adding members...")
        member1 = service.add_member("M001", "Alice")
        member2 = service.add_member("M002", "Bob")
        print("Members:", member1, member2)

        print("\nAdding books...")
        book1 = service.add_books("B001", "1984", "George Orwell", "1949")
        book2 = service.add_books("B002", "The Hobbit", "J.R.R. Tolkien", "1937")
        print("Books:", book1, book2)

        print("\nBorrowing a book...")
        service.borrow_book("L001", "M001", "B001")
        print(f"Book {book1.title} borrowed by {member1.name}")

        print("\nTrying to borrow the same book again...")
        service.borrow_book("L002", "M002", "B001")

    except LibraryException as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
