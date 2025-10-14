def add_book(library, title:str, author:str, isbn:str):
    if isbn in library:
        print(f"Cannot add: book with ISBN {isbn} already exists.")
        return 
    library[isbn] ={
        "title":title, 
        "author":author,
        "isbn":isbn,
        "available":True
    }
    print(f"Added: '{title}' by {author} (ISBN: {isbn}).")

def remove_book(library:dict, isbn:str):
    if isbn in library:
        del library[isbn]
        print(f"Removed: '{library[isbn]["title"]}' (ISBN: {isbn}).")
    else: 
        print(f"Cannot remove: ISBN {isbn} does not exist in the library.") 

def check_out_book(library, isbn):
    if isbn in library and library[isbn]["available"]==True:
        library[isbn]["available"]=False
    elif isbn in library and library[isbn]["available"]==False: 
        print(f"Cannot check out: '{library[isbn]["title"]}' (ISBN: {isbn}) is already checked out.")
        return
    else:  
        print(f"Cannot check out: ISBN {isbn} does not exist.")
        return


def return_book(library, isbn):
    if isbn in library and library[isbn]["available"]==True:
        print(f"Note: '{library[isbn]["title"]}' (ISBN: {isbn}) was already marked available.")
        return
    elif isbn not in library :
        print(f"Cannot return: ISBN {isbn} does not exist.")
        return
    library[isbn]["available"]=True
    print(f"Returned: '{library[isbn]["title"]}' (ISBN: {isbn}).")



def display_books(library):
    if not library:
        print("Library is empty.")
        return
    for book in library.values():
        if book["available"]==True:
            Availability = "Available" 
        else:
             Availability = "Checked Out"
        print(f"{book['title']} by {book['author']} (ISBN: {book['isbn']}) - {Availability}")
        



