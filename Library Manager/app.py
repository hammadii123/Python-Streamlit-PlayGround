import streamlit as st

if 'library' not in st.session_state:
    st.session_state.library = []


def add_book():
    title = st.text_input("Enter the book title:")
    author = st.text_input("Enter the author:")
    year = st.text_input("Enter the publication year:")
    genre = st.text_input("Enter the genre:")
    read_status = st.selectbox("Have you read this book?", ["Yes", "No"])

    if st.button("Add Book"):
        if title and author and year and genre:
            st.session_state.library.append({"title": title, "author": author, "year": year, "genre": genre, "read": read_status.lower() == "yes"})
            st.success("Book added successfully!")
        else:
            st.error("Please fill out all fields!")


def remove_book():
    title = st.text_input("Enter the title of the book to remove:")

    if st.button("Remove Book"):
        found_book = None
        for book in st.session_state.library:
            if book["title"].lower() == title.lower():
                found_book = book
                break

        if found_book:
            st.session_state.library.remove(found_book)
            st.success("Book removed successfully!")
        else:
            st.error("Book not found!")


def search_book():
    search_term = st.text_input("Enter the title or author to search:")

    if st.button("Search Book"):
        found_books = [book for book in st.session_state.library if search_term.lower() in book["title"].lower() or search_term.lower() in book["author"].lower()]

        if found_books:
            st.write("Matching Books:")
            for book in found_books:
                status = "Read" if book["read"] else "Unread"
                st.write(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
        else:
            st.warning("No matching books found.")


def display_books():
    if not st.session_state.library:
        st.write("Your library is empty!")
        return
    st.write("Your Library:")
    for book in st.session_state.library:
        status = "Read" if book["read"] else "Unread"
        st.write(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")


def display_statistics():
    total_books = len(st.session_state.library)
    if total_books == 0:
        st.write("No books in the library.")
        return
    read_books = len([book for book in st.session_state.library if book["read"]])
    read_percentage = (read_books / total_books) * 100
    st.write(f"Total books: {total_books}")
    st.write(f"Percentage read: {read_percentage:.2f}%")


def main():
    st.title("Personal Library Manager")

    menu = ["Add a Book", "Remove a Book", "Search for a Book", "Display All Books", "Display Statistics"]
    choice = st.sidebar.selectbox("Choose an option", menu)

    if choice == "Add a Book":
        add_book()
    elif choice == "Remove a Book":
        remove_book()
    elif choice == "Search for a Book":
        search_book()
    elif choice == "Display All Books":
        display_books()
    elif choice == "Display Statistics":
        display_statistics()

if __name__ == "__main__":
    main()























# # Normal logic
# library = []


# def add_book():
#     title = input("Enter the book title: ")
#     author = input("Enter the author: ")
#     year = input("Enter the publication year: ")
#     genre = input("Enter the genre: ")
#     read_status = input("Have you read this book? (yes/no): ").lower() == "yes"
    
    
#     library.append({"title": title, "author": author, "year": year, "genre": genre, "read": read_status})
#     print("Book added successfully!")




# def remove_book():
#     title = input("Enter the title of the book to remove: ")
#     for book in library:
#         if book["title"].lower() == title.lower():
#             library.remove(book)
#             print("Book removed successfully!")
#             return
#     print("Book not found!")

# #search for a book
# def search_book():
#     search_term = input("Enter the title or author to search: ")
#     found_books = [book for book in library if search_term.lower() in book["title"].lower() or search_term.lower() in book["author"].lower()]
    
#     if found_books:
#         print("Matching Books:")
#         for book in found_books:
#             status = "Read" if book["read"] else "Unread"
#             print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
#     else:
#         print("No matching books found.")




# # Function to display all books
# def display_books():
#     if not library:
#         print("Your library is empty!")
#         return
#     print("Your Library:")
#     for book in library:
#         status = "Read" if book["read"] else "Unread"
#         print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

# # Function to display statistics
# def display_statistics():
#     total_books = len(library)
#     if total_books == 0:
#         print("No books in the library.")
#         return
#     read_books = len([book for book in library if book["read"]])
#     read_percentage = (read_books / total_books) * 100
#     print(f"Total books: {total_books}")
#     print(f"Percentage read: {read_percentage:.2f}%")



# #show the menu
# def show_menu():
#     print("\nMenu")
#     print("1. Add a book")
#     print("2. Remove a book")
#     print("3. Search for a book")
#     print("4. Display all books")
#     print("5. Display statistics")
#     print("6. Exit")

# # Main function to run the program
# def main():
#     while True:
#         show_menu()
#         choice = input("Enter your choice: ")

#         if choice == "1":
#             add_book()
#         elif choice == "2":
#             remove_book()
#         elif choice == "3":
#             search_book()
#         elif choice == "4":
#             display_books()
#         elif choice == "5":
#             display_statistics()
#         elif choice == "6":
#             print("Goodbye!")
#             break
#         else:
#             print("Invalid choice! Please try again.")

# if __name__ == "__main__":
#     main()
