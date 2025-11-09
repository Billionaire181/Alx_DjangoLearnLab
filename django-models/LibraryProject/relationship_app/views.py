from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
from .models import Book 
def List_books(request):
	books = Book.objects.all()
	return render (request, 'relationship_app/list_books.html', {'books' : books} )

from django.views.generic.detail import DetailView
from .models import Library 

class LibraryDetailView(DetailView):
	model = Library
	template_name = 'relationship_app/library_detail.html'
	context_object_name = 'library'
	

form = UserCreationForm()
return render(request, 'relationship_app/register.html', {'form': form})
