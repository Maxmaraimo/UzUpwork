from typing import Any

from django.contrib import messages
from django.db import models
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.core.mail import send_mail


from .forms import BookForm
from .models import Books

# def publish_job(request):
#     if request.method == 'POST':
#         form = BookForm(request.POST, request.FILES)
#             book = form.save(commit=False)
#         if form.is_valid():
#             # book.author = request.user
#             book.save()
#             messages.success(request, 'Book added successfully!')
#             return redirect('books_view')
#     else:
#         form = BookForm()

#     context = {'form': form}
#     return render(request, 'publish_job.html', context)


class AddBookView(CreateView):
    modal = Books
    form_class = BookForm
    template_name = 'add_book.html'
    success_url = '/jobs/'

    def post(self, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            book = form.save(commit=False)
            book.author = self.request.user
            book.save()
        return redirect('books_view')


# def books(request):
#     context = {'books': Books.objects.all()}
#     return render(request, 'books.html', context)

class BooksListView(ListView):
    modal = Books
    template_name = 'books.html'

    def get_queryset(self):
        return Books.objects.all()


class BookDetailsView(DetailView):
    modal = Books
    template_name = 'work_details.html'

    def get_queryset(self):
        return Books.objects.filter(id=self.kwargs['pk'])


class BookUpdateView(UpdateView):
    modal = Books
    form_class = BookForm
    template_name = 'update_book.html'
    success_url = '/jobs/'

    def get_queryset(self):
        return Books.objects.filter(id=self.kwargs['pk'])



def delete_book(request, book_id: int):
    book = Books.objects.get(id=book_id)
    book.delete()
    messages.success(request, 'Work deleted successfully!')
    return redirect('books_view')


def send_email(request):
  email = request.POST['email']
  text = request.POST['text']

  send_mail(
    'Work details from Django',
    text,
    'ozodbekmahmaraimov16@gmail.com',
    [email],
  )



class BookDetailsViewTwo(DetailView):
    modal = Books
    template_name = 'submit.html'

    def get_queryset(self):
        return Books.objects.filter(id=self.kwargs['pk'])