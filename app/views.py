from django.shortcuts import render
from django.db.models import Min, Max, Avg, Count
from app.models import Author, Book


def index(request):

    authors = Author.objects.annotate(book_count=Count('books'))


    authors_count = Author.objects.aggregate(total_authors=Count('id'))

    return render(request, 'app/index.html', {
        'authors': authors,
        'total_authors': authors_count.get('total_authors', 0)
    })


def book_list(request):

    books = Book.objects.annotate(
        min_price=Min('price'),
        max_price=Max('price')
    ).filter(price__gt=5000)


    overall_stats = Book.objects.aggregate(
        avg_book_price=Avg('price'),
        min_book_price=Min('price'),
        max_book_price=Max('price')
    )

    return render(request, 'app/index.html', {
        'books': books,
        'avg_price': overall_stats.get('avg_book_price', 0),
        'min_price': overall_stats.get('min_book_price', 0),
        'max_price': overall_stats.get('max_book_price', 0)
    })
