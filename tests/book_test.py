import unittest
from models.book import Book

class TestBook(unittest.TestCase):

    def setUp(self):

        self.book = Book("Pillars of the Earth", "Ken Follet", "Historical Fiction")

    def test_book_has_title(self):
        self.assertEqual("Pillars of the Earth", self.book.title)

    def test_book_has_author(self):
        self.assertEqual("Ken Follet", self.book.author)

    def test_book_has_title(self):
        self.assertEqual("Historical Fiction", self.book.genre)



        