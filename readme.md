Contact Book

This is a Python project that creates a Contact Book. It implements CRUD (Create, Read, Update, Delete) operations to interact with the database. It also includes user authentication and backup features.

## Features

- **User Authentication**: Register or login to access the contact book.
- **CRUD Operations**: Insert, delete, update, and search contacts in the contact book.
- **Backup**: Backup your contact book to Google Drive.

## Usage

You can run the Contact Book with the following command:

```bash
python main.py <username> <password> <command> [arguments]
```
Replace `<username>` and `<password>` with your username and password for authentication. Replace `<command>` with one of the available commands. Some commands require additional arguments.

Here are the available commands:

- `insert`: Insert a new contact. Requires the name, address, phone, and email of the contact.
- `delete`: Delete a contact. Requires the phone number of the contact.
- `update`: Update a contact. Requires the previous phone number, and the new name, address, phone, and email of the contact.
- `search`: Search for a contact. Requires the phone number of the contact.
- `read`: Read all contacts. Optionally, you can specify an order.
- `backup`: Backup the contact book to Google Drive. No additional arguments required.

## Dependencies

This project uses the following Python libraries:

- `argparse`: For command line argument parsing.
- `ContactBook`: For managing the contact book.
- `validate`: For validating contact information.
- `Authentication.User`: For managing users.
- `Authentication.UserBook`: For managing the user database.
- `backup`: For backing up the contact book to Google Drive.
