from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
	path ('books/', list_books, name='list_books'),
	path ('library/<int:pk>/', LibraryDetailView.as_view(), name = 'library_detail'),
] 

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    # Login view
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),

    # Logout view
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Registration view (custom view)
    path('register/', views.register, name='register'),
]
