from flask import render_template, Blueprint, request, redirect
from models.book import Book
from models.books import books

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/")
def index():
    return render_template("index.html", title="Lou Lou's Library", books=books)

@books_blueprint.route('/books')
def book_list():
    return render_template("books/index.html", books=books)

@books_blueprint.route("/books/<index>")
def single_book(index):
    book = books[int(index)]
    return render_template("/show.html", book=book, index=index)

@books_blueprint.route("/books", methods=['POST'])
def add_book():
    
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]
    checked_out = "checked_out" in request.form
    added_book = Book(title, author, genre, checked_out)
    books.append(added_book)
    return redirect("/books")

@books_blueprint.route("/books/new")
def books_added():
    return render_template("books/new.html")

@books_blueprint.route("/books/delete/<index>", methods=["POST"])
def delete_book(index):
        book = books[int(index)]
        books.remove(book)
        return redirect("/books")

@books_blueprint.route("/books/<index>", methods=["POST"])
def update_book(index):
     book = books[int(index)]
     checked_out = "checked_out" in request.form
     book.checked_out = checked_out
     return redirect("/books/" + index)


