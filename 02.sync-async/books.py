from fastapi import APIRouter
from typing import List
from models import Book, CreateBook, SearchBooks
from typing import Optional

route = APIRouter()
books: List[Book] = [] # [Book, Book, Book, ...]

@route.post('/')
def create_book(book: CreateBook) -> Book:
    book = Book(id=len(books)+1, **book.model_dump())
    books.append(book)

    return book

@route.get('/search/')
# def search_book() -> SearchBook:
#     pass
def search_books(keyword: Optional[str], max_results: int = 10) -> SearchBooks: # [Book, Book, Book, ...]
    search_result = [book for book in books if keyword in book.title] if keyword else books

    # for book in books:
    #     if keyword in book.title:
    #         book

    # max_result: pageination을 위한 옵션
    return SearchBooks(results=search_result[:max_results])