from typing import List, Optional

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

class Book:
    def __init__(self, id_: int, name: str, pages: int):
        self.id = id_
        self.name = name
        self.pages = pages

    def __repr__(self):
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"

class Library:
    def __init__(self, books: Optional[List[Book]] = None):
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self) -> int:
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError(f"Книги с запрашиваемым id {book_id} не существует")

if __name__ == '__main__':
    empty_library = Library()
    print(empty_library.get_next_book_id())
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)
    print(library_with_books.get_next_book_id())
    print(library_with_books.get_index_by_book_id(1))