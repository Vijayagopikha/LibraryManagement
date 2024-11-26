from django.core.mail import send_mail
from django.utils.timezone import now
from datetime import timedelta
from .models import BorrowedBook, Signup

def send_due_date_notifications():
    # Get current date
    today = now()

    # Get all borrowed books where due date is within 10 days
    books_due_soon = BorrowedBook.objects.filter(
        due_date__gt=today, 
        due_date__lte=today + timedelta(days=10)
    )

    # Loop through all the books and send email notifications
    for book in books_due_soon:
        user = book.user
        # Send email to the user
        send_mail(
            'Your borrowed book is due soon',
            f"Dear {user.username},\n\nYour book '{book.book_name}' is due on {book.due_date}. Please return it soon.",
            'no-reply@yourwebsite.com',  # Use your website's email address
            [user.email],  # The user's email address
            fail_silently=False,
        )
