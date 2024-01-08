from django.urls import path

from test_task.main.views import BookListView

urlpatterns = [
    path('', BookListView.as_view(), name='books'),
]
