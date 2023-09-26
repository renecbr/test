from datetime import datetime

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    book_objects = Book.objects.all()
    context = {
        'books': book_objects,
    }
    return render(request, template, context)


def books_pag_view(request, pub_date):
    template = 'books/books_list.html'
    all_book = Book.objects.all().order_by('pub_date')
    dates = []
    for b in all_book:
        dates.append(b.pub_date)
    d = datetime.strptime(pub_date, '%Y-%m-%d').date()
    if d in dates:
        pr_d = Book.objects.filter(pub_date__lt=pub_date).first()
        next_d = Book.objects.filter(pub_date__gt=pub_date).first()
        book_objects = Book.objects.filter(pub_date=d)
        paginator = Paginator(all_book, 10)
        context = {
            'books': book_objects,
            'pub_date': d,
            'pr_d': pr_d,
            'next_d': next_d,
        }
        return render(request, template, context)
    else:
        msg = f'В библиотеке нету книг с датой: {pub_date}'
        return HttpResponse(msg)







