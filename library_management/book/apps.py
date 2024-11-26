from django.apps import AppConfig
from django.core.mail import send_mail


class BookConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'book'
    def ready(self):
        borrowed_books = [
        {'book_name': 'Materials Engineering', 'due_date': '2024-12-05 04:32:31'},
        {'book_name': 'Mechanical Book', 'due_date': '2024-12-05 04:47:49'},
        ]

            # Start the HTML table for the email content
        table_content = """
        <table border="1" style="border-collapse: collapse; width: 100%; text-align: left;">
            <tr>
                <th>Book Name</th>
                <th>Due Date</th>
            </tr>
        """

        # Add rows for each borrowed book from the static list
        for book in borrowed_books:
            table_content += f"""
            <tr>
                <td>{book['book_name']}</td>
                <td>{book['due_date']}</td>
            </tr>
            """

        # Close the table
        table_content += "</table>"

        # Email subject and message
        subject = 'Your Borrowed Due Book Dates'
        message = f"""
        <p>This is an automated email triggered by the app startup. Below is the list of borrowed books with their due dates:</p>
        {table_content}
        """
        
        recipient_list = ['vijayagopikhas.22cse@kongu.edu','vanjulas.22cse@kongu.edu']
        
        # Send the email with HTML content
        send_mail(
            subject,
            message,
            'vijayagopikhas.22cse@kongu.edu',
            recipient_list,
            html_message=message  # Include the HTML version of the message
        )
        