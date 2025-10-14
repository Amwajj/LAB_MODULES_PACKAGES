import dateOP
from library import librarian

def check_input_nonempty(msg):
    while True:
        value = input(msg).strip()
        if value:
            return value
        print("Input cannot be empty. Try again.")

def main():
    
   

    menu = """
    1- Add a book to the library
    2- Remove a book from the library
    3- Check out a book
    4- Return a book
    5- Display all books
    6- Exit
    """

    library = {}

    while True:
        print(menu)
        choice_raw = input("Your choice (1-6): ").strip()
        if not choice_raw.isdigit():
            print("Please enter a number from 1 to 6.")
            continue

        user_choice = int(choice_raw)

        if user_choice == 1:
            title = check_input_nonempty("Title: ")
            author = check_input_nonempty("Author: ")
            isbn = check_input_nonempty("ISBN: ")
            librarian.add_book(library, title, author, isbn)

        elif user_choice == 2:
            isbn = check_input_nonempty("ISBN to remove: ")
            librarian.remove_book(library, isbn)

        elif user_choice == 3:
            isbn = check_input_nonempty("ISBN to check out: ")
            librarian.check_out_book(library, isbn)

        elif user_choice == 4:
            isbn = check_input_nonempty("ISBN to return: ")
            librarian.return_book(library, isbn)

        elif user_choice == 5:
            librarian.display_books(library)

        elif user_choice == 6:
            print("Goodbye, my friend. Come every day!")
            break

        else:
            print("Invalid option. Please choose between 1 and 6.")

if __name__ == "__main__":
    main()
