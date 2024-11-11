
---

# Phonebook Application 📞

This is a simple, interactive Phonebook Application built with Python. The application allows users to manage a personal contact list with ease, performing essential actions like adding, searching, deleting, and listing contacts.

## Features

- **Add a New Contact**: Easily add contacts by entering a name and phone number. If the contact already exists, the application will notify you.
- **Search for a Contact**: Quickly search for any contact by name and get the associated phone number.
- **Delete a Contact**: Remove any contact by name, with a message confirming the deletion.
- **List All Contacts**: View a complete list of saved contacts, displayed in a user-friendly format.
- **Exit**: Close the application gracefully.

This project reinforces core Python skills, especially in handling dictionaries, conditional statements, and basic user interface design.

## Getting Started

### Prerequisites

- **Python 3.x**: Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/).

### Installation

1. Clone this repository or download the `phonebook.py` file.
2. Open a terminal and navigate to the directory containing `phonebook.py`.

### Running the Application

Run the following command in your terminal:

```bash
python phonebook.py
```

This will launch the Phonebook Application and display a menu where you can choose an action by entering the corresponding number.

## Project Structure

- **phonebook.py**: This is the main script file containing the application’s code. It defines the functions for adding, searching, deleting, and listing contacts, as well as a main loop to display the menu and take user input.

## How It Works

The application uses a Python dictionary to store contact information, where each contact’s name is the key and their phone number is the value. This structure enables efficient lookups, additions, deletions, and listings of contacts. The `if __name__ == "__main__":` check ensures that the application runs only when executed directly, allowing the code to be reusable as a module if needed.

### Functions Overview

- **add_contact()**: Prompts the user for a name and phone number, adds the contact if it doesn't already exist.
- **search_contact()**: Searches for a contact by name and displays the phone number if found.
- **delete_contact()**: Deletes a contact by name if it exists in the phonebook.
- **list_contacts()**: Lists all contacts in the phonebook with names and phone numbers.

## Usage Example

1. Run the application.
2. Choose an action from the menu:
   - Press **1** to add a new contact.
   - Press **2** to search for an existing contact.
   - Press **3** to delete a contact.
   - Press **4** to list all contacts.
   - Press **5** to exit the application.

## Project Goals

This project is designed as a learning tool to practice basic Python skills, focusing on:
- Using dictionaries for data storage.
- Implementing conditional logic for user actions.
- Structuring code with functions for better readability and reusability.
  
## License

This project is free to use and modify. Feel free to enhance or customize the code according to your needs.

---
