import argparse
from ContactBook import ContactBook
from validate import validation
from Authentication.User import User
from Authentication.UserBook import UserBook
from backup import upload_file_to_drive


def main():
    userbook = UserBook()  # Create users database
    args = parsear()
    name, password = args.authentication
    user = User(name, password)  # Create user (name,pass)
    author = userbook.login(
        user.user, user.password
    )  # Login  (return name if already exists or is registered /// raise a ValueError if password is incorrect)

    contact_book = ContactBook(author)
    if args.command == "insert":
        name, address, phone, email = args.insert
        validation(name, address, phone, email)
        contact_book.insert(name, address, phone, email)
        print("Contact inserted")
    elif args.command == "delete":
        phone = args.delete[0]
        validation(phone=phone)
        contact_book.delete(phone)
    elif args.command == "update":
        prev_phone, name, address, phone, email = args.update
        validation(name, address, phone, email, prev_phone)
        contact_book.update(prev_phone, name, address, phone, email)
    elif args.command == "search":
        phone = args.search[0]
        validation(phone=phone)
        contact_book.search(phone)
    elif args.command == "read":
        if not args.order:
            contact_book.read()
        else:
            contact_book.read(args.order)
    elif args.command == "backup":
        upload_file_to_drive()


def parsear():
    parser = argparse.ArgumentParser(
        prog="Contact Book",
        description="Python project that creates a Contact Book. It implements CRUD to interact with the database.",
        epilog="Thanks for your time. :DD",
    )
    parser.add_argument(
        "authentication",
        nargs=2,
        # metavar=('name', 'password'),  This line gives a bug
        help="Register or login",
        type=str,
    )
    subparsers = parser.add_subparsers(dest="command", help="Available command")

    # Insert command
    insert_parser = subparsers.add_parser("insert", help="Insert a new contact")
    insert_parser.add_argument(
        "insert",
        nargs=4,
        metavar=("name", "address", "phone", "email"),
        help="Insert a contact specifying the name, address, phone and email",
    )

    # Update command
    update_parser = subparsers.add_parser("update", help="Update a contact")
    update_parser.add_argument(
        "update",
        nargs=5,
        metavar=("previous_phone", "name", "address", "phone", "email"),
        help="Update a contact based on his old phone.",
    )

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a contact")
    delete_parser.add_argument(
        "delete",
        metavar="Phone",
        nargs=1,
        help="Delete a contact by phone",
    )

    # Search command
    search_parser = subparsers.add_parser("search", help="Search a contact")
    search_parser.add_argument(
        "search", metavar="phone", nargs=1, help="Search a contact by phone"
    )

    # Read command
    read_parser = subparsers.add_parser("read", help="Read the contact book")
    read_parser.add_argument(
        "--order",
        metavar=("name or timestamp"),
        choices=["name", "change_at"],
        help="Order by: name or timestamp ",
    )

    # Backup command
    backup_parser = subparsers.add_parser("backup", help="Search a contact")
    return parser.parse_args()


if __name__ == "__main__":
    main()
