from django.views import generic

from test_task.main.models import Book


class BookListView(generic.ListView):
    model = Book
