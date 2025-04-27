import json
import os

class Library:
    def __init__(self):
        self._books = self.load_books()

    def load_books(self):
        if os.path.exists("library.json"):
            with open("library.json", "r") as f:
                return json.load(f)
        return {}

    def save_books(self):
        with open("library.json", "w") as f:
            json.dump(self._books, f, indent=4)

    def add_book(self, title):
        if title in self._books:
            print(f"'{title}' already exists.")
        else:
            self._books[title] = {"available": True, "borrowed_by": None}
            self.save_books()
            print(f"Book '{title}' added to library.")

class Student(Library):
    def borrow_book(self, title, student_name):
        if title in self._books:
            if self._books[title]["available"]:
                self._books[title]["available"] = False
                self._books[title]["borrowed_by"] = student_name
                self.save_books()
                print(f"{student_name} borrowed '{title}'.")
            else:
                print(f"'{title}' is already borrowed by {self._books[title]['borrowed_by']}.")
        else:
            print(f"'{title}' does not exist in library.")

    def return_book(self, title, student_name):
        if title in self._books:
            if not self._books[title]["available"] and self._books[title]["borrowed_by"] == student_name:
                self._books[title]["available"] = True
                self._books[title]["borrowed_by"] = None
                self.save_books()
                print(f"{student_name} returned '{title}'.")
            else:
                print(f"Cannot return '{title}'. You didn't borrow .")
        else:
            print(f"'{title}' does not exist.")

def main():
    lib = Student()

    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            lib.add_book(title)

        elif choice == "2":
            title = input("Enter book title to borrow: ")
            name = input("Enter your name: ")
            lib.borrow_book(title, name)

        elif choice == "3":
            title = input("Enter book title to return: ")
            lib.return_book(title)

        elif choice == "4":
            print("exit!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
