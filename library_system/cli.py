from library_service import LibraryService, LibraryException
from repositories import InMemoryBookRepository, InMemoryMemberRepository, InMemoryLoanRepository

def populate_sample_data(service: LibraryService):
    # Add some members
    try:
        service.add_member("M001", "aaa")
        service.add_member("M002", "bbb")
        service.add_member("M003", "ccc")
    except LibraryException:
        pass  # ignoring if already exists

    # Add some books
    try:
        service.add_books("B001", "1984", "abc cba", "1949")
        service.add_books("B002", "yyyy", "dsj jdkds", "1937")
        service.add_books("B003", "sasa", "sdsds dkds", "1960")
        service.add_books("B004", "bbab", "dsk dskk", "1813")
    except LibraryException:
        pass  # ignoring if already exists

def main():
    book_repo = InMemoryBookRepository()
    member_repo = InMemoryMemberRepository()
    loan_repo = InMemoryLoanRepository()

    service = LibraryService()
    service.books = book_repo
    service.members = member_repo
    service.loans = loan_repo

    populate_sample_data(service)

    while True:
        print("\n===== Library Menu =====")
        print("1. Add Member")
        print("2. Add Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. List All Members")
        print("6. List All Books")
        print("0. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                member_id = input("Enter member ID: ")
                name = input("Enter member name: ")
                member = service.add_member(member_id, name)
                print(f"Member added: {member}")

            elif choice == "2":
                book_id = input("Enter book ID: ")
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                year = input("Enter book year: ")
                book = service.add_books(book_id, title, author, year)
                print(f"Book added: {book}")

            elif choice == "3":
                loan_id = input("Enter loan ID: ")
                member_id = input("Enter member ID: ")
                book_id = input("Enter book ID: ")
                service.borrow_book(loan_id, member_id, book_id)
                book = service.books.get_by_id(book_id)
                print(f"Book '{book.title}' borrowed by member '{member_id}'")

            elif choice == "4":
                loan_id = input("Enter loan ID: ")
                member_id = input("Enter member ID: ")
                book_id = input("Enter book ID: ")
                book = service.return_book(loan_id, member_id, book_id)
                print(f"Book '{book.title}' returned successfully.")

            elif choice == "5":
                members = service.members.list_all_members()
                print("Members:")
                for m in members:
                    print(f"ID: {m.member_id}, Name: {m.name}")

            elif choice == "6":
                books = service.books.list_all_books()
                print("Books:")
                for b in books:
                    status = "Available" if b.is_available() else f"Borrowed by {b.book_lend_member_id}"
                    print(f"ID: {b.book_id}, Title: {b.title}, Author: {b.author}, Year: {b.year}, Status: {status}")

            elif choice == "0":
                print("Exiting... Goodbye!")
                break

            else:
                print("Invalid choice. Try again.")

        except LibraryException as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
