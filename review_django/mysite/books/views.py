from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from books.models import Book, Author, Publisher 
# Create your views here.

class BookModelView(TemplateView):
  template_name = 'books/index.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)          # get_context_data를 사용하기위해 반드시 작성되어야하는 부분
    context['model_list'] = ['Book', 'Author', 'Publisher']
    return context

class BookList(ListView):
  model = Book

class AuthorList(ListView):
  model = Author

class PublisherList(ListView):
  model = Publisher

class BookDetail(DetailView):
  model = Book

class AuthorDetail(DetailView):
  model = Author

class PublisherDetail(DetailView):
  model = Publisher