Contact Book Manager (CLI)

A command-line contact management application built in Python. Add, view, search, update, and delete contacts — all persisted to a local JSON file so your data survives between runs.

Built as a hands-on project to apply core Python fundamentals: OOP, exception handling, file I/O, and JSON serialization.

Features


Add new contacts with auto-generated unique IDs
View all saved contacts
Search contacts by name
Update a contact's name, phone number, or email
Delete a contact
Persistent storage — contacts are saved to contacts.json on exit and automatically reloaded the next time the program runs


Tech / Concepts Used


Object-Oriented Programming — a Contact class with encapsulated (private) attributes and getter methods
Class attributes — used to auto-generate sequential, unique contact IDs
File I/O & JSON — json.load() / json.dump() for reading and writing contact data
Exception handling — try / except FileNotFoundError to gracefully handle a first run with no saved data
Match-case statements — Python 3.10+ pattern matching used for the menu-driven interface


How to Run

Requirements: Python 3.10 or higher (for match/case support)

bashgit clone https://github.com/Manjunath0055/Contact-Book-Manager-CLI-.git
cd Contact-Book-Manager-CLI-
python main.py

No external dependencies — uses only Python's standard library (json).

Usage

On launch, you'll see a menu:

-- Operations --
1. Add new contact
2. View all contacts
3. Search contact
4. Update contact
5. Delete contact
6. Save and Exit

Enter the number corresponding to the action you want. Choosing 6 saves all contacts to contacts.json and exits — reopening the program will automatically reload them.

Project Structure

Contact-Book-Manager-CLI
─ main.py          # Main application logic
─ contacts.json     # Auto-generated on first save (contact data)
─ README.md

Possible Future Improvements


Input validation (e.g. reject empty names, non-numeric phone numbers)
Duplicate contact detection
Sort/export contacts (e.g. to CSV)



Built while learning Python fundamentals — OOP, file handling, and exception handling.
