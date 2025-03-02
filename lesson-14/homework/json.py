#puzzle 1
import json
with open("students.json", "r") as file:
    students = json.load(file)
for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
#puzzle 2
import requests

API_KEY = "your_api_key" 
CITY = "Tashkent"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
if response.status_code == 200:
    data = response.json()
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Weather: {data['weather'][0]['description']}")
else:
    print("Error fetching data.")
#puzzle 3
import json

# Load books.json
try:
    with open("books.json", "r") as file:
        books = json.load(file)
except FileNotFoundError:
    books = []

def save_books():
    with open("books.json", "w") as file:
        json.dump(books, file, indent=4)

def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    year = input("Enter publication year: ")
    books.append({"title": title, "author": author, "year": year})
    save_books()
    print("Book added!")

def update_book():
    title = input("Enter the title of the book to update: ")
    for book in books:
        if book["title"].lower() == title.lower():
            book["author"] = input("Enter new author: ")
            book["year"] = input("Enter new year: ")
            save_books()
            print("Book updated!")
            return
    print("Book not found.")

def delete_book():
    title = input("Enter the title of the book to delete: ")
    global books
    books = [book for book in books if book["title"].lower() != title.lower()]
    save_books()
    print("Book deleted!")

while True:
    print("\n1. Add Book\n2. Update Book\n3. Delete Book\n4. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        add_book()
    elif choice == "2":
        update_book()
    elif choice == "3":
        delete_book()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Try again.")
  #puzzle 4
  import requests
import random

API_KEY = "your_omdb_api_key"  # Get your API key from http://www.omdbapi.com/
GENRE = input("Enter a movie genre (Action, Comedy, Drama, etc.): ")

MOVIES = {
    "Action": ["Mad Max: Fury Road", "Die Hard", "John Wick"],
    "Comedy": ["Superbad", "The Hangover", "Step Brothers"],
    "Drama": ["Forrest Gump", "The Shawshank Redemption", "Fight Club"]
}

if GENRE in MOVIES:
    movie = random.choice(MOVIES[GENRE])
    URL = f"http://www.omdbapi.com/?t={movie}&apikey={API_KEY}"
    
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        print(f"Title: {data['Title']}")
        print(f"Year: {data['Year']}")
        print(f"IMDB Rating: {data['imdbRating']}")
        print(f"Plot: {data['Plot']}")
    else:
        print("Error fetching movie details.")
else:
    print("Genre not found.")



