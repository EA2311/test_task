from django.urls import path

from test_task.main.views import BookListView

app_name = 'main'

urlpatterns = [
    path('', BookListView.as_view(), name='books'),
]
