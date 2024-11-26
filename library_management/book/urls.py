"""
URL configuration for library_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
   
   path('', views.homepage, name='homepage'),  # Set this as the home page
    path('login/', views.login, name='login'),
      # Root URL
    #path('search/', views.search_books, name='search_books'), 
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path('add',views.add, name = 'add'),
    
    path('update/<int:book_id>/<str:book_type>/',views.update,name = 'update'),
    path('delete/<int:book_id>/<str:book_type>/', views.delete, name='delete'),
    
   # path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('borrow/<int:book_id>/<str:book_type>/', views.borrow_book, name='borrow_book'),
    path('borrowed-books/', views.borrowed_books, name='borrowed_books'),
    path('return/<int:book_id>/', views.return_book, name='return_book'),

   #for admin
   path('borrowed-books-admin/', views.borrowed_books_list, name='borrowed_books_list'),

]


#for imges
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


