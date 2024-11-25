from django.shortcuts import render, get_object_or_404, redirect

from django.db.models import Q
from .models import TechnicalBook, GeneralBook, Signup , BorrowedBook
from datetime import timedelta
from datetime import datetime, timedelta

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def homepage(request):
    return render(request, 'homepage.html', {'show_nav': False})


def home(request):
    if 'user_id' not in request.session:
        return redirect('login')

    search_query = request.GET.get('q', '')
    filter_by = request.GET.get('filter_by', 'book_name')

    technical_books = TechnicalBook.objects.all()  # Fetch all technical books
    general_books = GeneralBook.objects.all()  # Fetch all general books

    # Apply search filtering based on the filter criteria
    if search_query:
        if filter_by == 'book_name':
            # Filter both technical and general books by book name
            technical_books = technical_books.filter(book_name__icontains=search_query)
            general_books = general_books.filter(book_name__icontains=search_query)
        elif filter_by == 'author':
            # Filter both technical and general books by author
            technical_books = technical_books.filter(author__icontains=search_query)
            general_books = general_books.filter(author__icontains=search_query)
        elif filter_by == 'departname':
            # Only filter technical books by department name, leave general books unchanged
            technical_books = technical_books.filter(departname__icontains=search_query)
            general_books = GeneralBook.objects.none()  # Return an empty queryset for general books when filtering by department

    user_id = request.session.get('user_id')

    if user_id == -1:  # Admin
        return render(request, 'index.html', {
            'technical_books': technical_books, 
            'general_books': general_books, 
            'isadmin': True, 
            'show_nav': False
        })
    else:  # Regular user
        user = Signup.objects.get(id=user_id)
        return render(request, 'userindex.html', {
            'technical_books': technical_books, 
            'general_books': general_books, 
            'isadmin': user.isadmin, 
            'show_nav': False
        })



@csrf_exempt
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return render(request, 'signup.html', {'error': 'Passwords do not match', 'show_nav': False})
        
        if Signup.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return render(request, 'signup.html', {'error': 'Email already exists', 'show_nav': False})

        user = Signup(username=username, email=email, password=password, confirm_password=confirm_password)
        if email == "adminkec@gmail.com":
            user.isadmin = True
        user.save()
        messages.success(request, 'Account created successfully!')
        return redirect('login')
    
    return render(request, 'signup.html', {'show_nav': False})

@csrf_exempt
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if email == "adminkec@gmail.com" and password == "library":
            request.session['user_id'] = -1  # Using -1 for admin
            messages.success(request, 'Login successful!')
            return redirect('home')
        try:
            user = Signup.objects.get(email=email, password=password)
            request.session['user_id'] = user.id
            messages.success(request, 'Login successful!')
            if user.isadmin:
                return redirect('admin_home')
            else:
                return redirect('home')
        except Signup.DoesNotExist:
            messages.error(request, 'Invalid email or password')
            return render(request, 'login.html', {'error': 'Invalid email or password'})
    
    return render(request, 'login.html', {'show_nav': False})

def logout(request):
    request.session.flush()
    messages.success(request, 'Logged out successfully!')
    return redirect('login')

@csrf_exempt
def add(request):
    if 'user_id' not in request.session:
        return redirect('login')

    if request.method == "GET":
        return render(request, 'add.html')
    elif request.method == "POST":
        book_type = request.POST['book_type']
        book_name = request.POST['book_name']
        author = request.POST['author']
        department_name = request.POST.get('department_name', '')
        edition = request.POST.get('edition', '')
        num_available = int(request.POST['num_available'])
        image_url = request.POST.get('image_url', '')
        online_url = request.POST.get('online_book_url', '')  # New field for online book URL
        print(online_url)
        if book_type == 'technical':
            department_name  = request.POST.get('departname_name','')
            TechnicalBook.objects.create(
                departname=department_name,
                book_name=book_name,
                author=author,
                edition=edition,
                book_available = num_available,
                image_url=image_url,
                online_book_url=online_url  # Store the online URL in the database
            )
        elif book_type == 'general':
            category  = request.POST.get('category','')
            GeneralBook.objects.create(
                category=category,
                book_name=book_name,
                author=author,
                book_available = num_available,
                image_url=image_url,
                online_book_url=online_url  # Store the online URL in the database
            )
        messages.success(request, 'Book added successfully!')
        return redirect('home')  # Redirect to the books list view

@csrf_exempt
def update(request, book_id, book_type):
    if 'user_id' not in request.session:
        return redirect('login')

    if book_type == 'technical':
        book = get_object_or_404(TechnicalBook, id=book_id)
    elif book_type == 'general':
        book = get_object_or_404(GeneralBook, id=book_id)

    if request.method == 'POST':
        book.book_name = request.POST['book_name']
        book.author = request.POST['author']
        if book_type == 'technical':
            book.departname = request.POST.get('department_name', '')
            book.edition = request.POST.get('edition', '')
        elif book_type == 'general':
            book.category = request.POST.get('category', '')
        book.book_available = int(request.POST['num_available'])
        book.image_url = request.POST.get('image_url', '')
        book.online_url = request.POST.get('online_url', '')  # New field for online book URL
        book.save()
        messages.success(request, 'Book updated successfully!')
        return redirect('home')  # Redirect to the books list view

    return render(request, 'update.html', {'book': book, 'book_type': book_type, 'show_nav':True})

@csrf_exempt
def delete(request, book_id, book_type):
    if 'user_id' not in request.session:
        return redirect('login')

    if book_type == 'technical':
        book = get_object_or_404(TechnicalBook, id=book_id)
    elif book_type == 'general':
        book = get_object_or_404(GeneralBook, id=book_id)

    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully!')
        return redirect('home')  # Redirect to the books list view

    return render(request, 'delete.html', {'book': book, 'book_type': book_type, 'show_nav':True})





def borrow_book(request, book_id, book_type):
    if 'user_id' not in request.session:
        return redirect('login')

    user_id = request.session['user_id']
    user = Signup.objects.get(id=user_id)

    if book_type == 'technical':
        book = get_object_or_404(TechnicalBook, id=book_id)
    else:
        book = get_object_or_404(GeneralBook, id=book_id)
    
    due_date =  datetime.now()+ timedelta(days=9)
    borrow_date=datetime.now()
    borrowed_book = BorrowedBook(
        user=user,
        book_name=book.book_name,
        book_type=book_type,
        borrow_date=borrow_date,
        due_date=due_date
    )
    borrowed_book.save()
    return redirect('/home')


def borrowed_books(request):
    if request.method=="GET":
        if 'user_id' not in request.session:
            return redirect('login')

        user_id = request.session['user_id']
        borrowed_books = BorrowedBook.objects.filter(user_id=user_id)

        # Add due dates dynamically
        for book in borrowed_books:
            book.due_date = book.borrow_date + timedelta(days=9)

        return render(request, 'borrowed_books.html', {'borrowed_books': borrowed_books})


def return_book(request, book_id):
    if 'user_id' not in request.session:
        return redirect('login')

    user_id = request.session['user_id']
    borrowed_book = get_object_or_404(BorrowedBook, id=book_id, user_id=user_id)
    
    # Delete the borrowed book from the database
    borrowed_book.delete()

    # Optionally, show a success message
    messages.success(request, 'Book returned successfully!')

    # Redirect the user back to the borrowed books list
    return redirect('borrowed_books')


