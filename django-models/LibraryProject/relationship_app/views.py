from django.shortcuts import render

# Create your views here.
from .models import Book 
def Book_list(request):
	books = Book.objects.all()
	return render (request, 'relationship_app/book_list.html', {'books' : books} )

from django.views.generic import DetailView
from .models import Library 

class LibraryDetailView(DetailView):
	model = Library
	template_name = 'relationship_app/book_detail.html'
	context_object_name = 'library'
 
