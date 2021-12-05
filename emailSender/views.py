from django.shortcuts import render
from utilities.EmailService import EmailService

# Create your views here.


def home_page(request):
    if request.method == "POST":
        subject = request.POST.get('subject')
        emails = request.POST.get('emails')
        title = request.POST.get('title')
        description = request.POST.get('message')
        EmailService.send_email(
            subject,
            emails.split(','),
            'emails/email_template.html',
            {
                'title': title,
                'description': description
            }
        )
    return render(request, 'email_form.html')
