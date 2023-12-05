from django.urls import path

from .views import *

urlpatterns = [
    path("", BooksListView.as_view(), name="books_view"),
    path("add_job", AddBookView.as_view(), name="add_job"),
    path("update_book/<int:pk>", BookUpdateView.as_view(), name="update_book"),
    path("work_details/<int:pk>", BookDetailsView.as_view(), name="work_details"),
    path("submit/<int:pk>", BookDetailsViewTwo.as_view(), name="submit"),
    path("delete_book/<int:book_id>", delete_book, name="delete_book"),
    path("send_email/<int:book_id>", send_email, name="send_email"),
    

]