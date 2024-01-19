
# Add a book to the library
def add_book(book):
    with open("Library.txt", "a") as f:
        f.write(f"{book['title']}, {book['author']}, {book['year']}, {book['rating']}, {book['pages']}\n")


# Accesses a book from the library by title
def access_single_book(search_method, input):
    with open("Library.txt", "r") as f:
        file = f.readlines()
        if search_method == "title":
            for line in file:
                title, author, year, rating, pages = line.split(", ")
                if title == input: 
                    book = {
                        "title": title,
                        "author": author,
                        "year": int(year),
                        "rating": float(rating),
                        "pages": int(pages)
                    }
                    print(f"Here is {book['title']}, written in {book['year']} by {book['author']}. It has a rating of {book['rating']} and {book['pages']} total pages, enjoy!\n")
        elif search_method == 'author':
            for line in file:
                title, author, year, rating, pages = line.split(", ")
                if  author == input: 
                    book = {
                        "title": title,
                        "author": author,
                        "year": int(year),
                        "rating": float(rating),
                        "pages": int(pages)
                    }
                    print(f"Here is {book['title']}, written in {book['year']} by {book['author']}. It has a rating of {book['rating']} and {book['pages']} total pages, enjoy!\n")
        

# Returns all books from the library
def access_all_books():
    with open("Library.txt", "r") as f:
        file = f.readlines()
        for line in file:
            title, author, year, rating, pages = line.split(", ")
            book = {
                "title": title,
                "author": author,
                "year": int(year),
                "rating": float(rating),
                "pages": int(pages)
            }
            print(f"{book['title']}, written in {book['year']} by {book['author']}. A rating of {book['rating']} and {book['pages']} total pages.\n")  


# Returns the average rating of all books
def average_rating():
    with open("Library.txt", "r") as f:
        file = f.readlines()
        rating_list = []
        avg_rating = 0
        for line in file:
            title, author, year, rating, pages = line.split(", ")
            rating_list.append(float(rating))   
        avg_rating = sum(rating_list) / len(rating_list)
        print(f'The average rating of all books is {avg_rating}\n')


# Get users book input
def get_user_book():
    title = input("What is the title of this book? \n\n")
    print("")
    author = input("Who is the author of this book? \n\n")
    print("")
    while True:
        try:
            year = int(input("When was this book published? \n\n"))
            print("")
            break
        except ValueError:
            print("")
            print("Please enter a number for when the book was published. \n\n")
    while True:
        try:
            rating = float(input("What is the rating of this book? \n\n"))
            print("")
            break
        except ValueError:
            print("")
            print("Please enter a number for the rating. \n\n")
    while True:
        try:
            pages = int(input("How many pages are in this book? \n\n"))
            print("")
            break
        except ValueError:
            print("")
            print("Please enter a number for the total pages. \n\n")
    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }
    return book_dictionary

# Menu for how you want to access books
def book_access_menu():
    book_menu = True
    while book_menu:
        user_input = input("        Book Access    \n-----------------------------\n - TITLE: Access a book by title\n - AUTHOR: See all books by an author\n - ALL BOOKS: See all your books\n - AVG RATING: See the average rating of your books\n - BACK: back to main menu\n\n").lower()
        print("")
        if user_input == "title":
            title_input = input("what is the title of the book?\n\n")
            print("")
            access_single_book('title', title_input)
            book_access_menu()
        elif user_input == "all books":
            access_all_books()
            book_access_menu()
        elif user_input == "author":
            author_input = input("Who is the author of the books?\n\n")
            print("")
            access_single_book('author', author_input)
            book_access_menu()
        elif user_input == "avg rating":
            average_rating()
            book_access_menu()
        elif user_input == "back":
            book_menu = False
            home_screen()
        else:
            print("Please enter the correct input.\n\n")

# Keep asking user for books
def ask_for_book():
    adding_books = True
    while adding_books:
        book = get_user_book()
        add_book(book)
        user_input = input("Would you like to add another book? \n\n").lower()
        print("")
        if user_input == "yes":
            pass
        elif user_input == "no":
            adding_books = False
            book_access_menu()
        else:
            print("Please input either 'Yes' or 'No'. \n\n")


# Ask user what they want to do
def home_screen():
    getting_input = True
    while getting_input:
        user_input = input("        Menu    \n---------------------\n - ADD: Add a book\n - ACCESS: Access books\n\n").lower()
        print("")
        if user_input == "add":
            getting_input = False
            ask_for_book()
        elif user_input == "access":
            getting_input = False
            book_access_menu()
        else: 
            print("Please input either 'Add' or 'Get'. \n\n")


# Welcome the user and start the program
if __name__ == "__main__":
    print("\n\nWelcome to the library! \n\n")
    home_screen()