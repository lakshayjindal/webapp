from django.shortcuts import render
from .models import Contact
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['mob']
        address = request.POST['address']
        issue = request.POST['Issue']
        objectInstance = Contact()
        objectInstance.Name = name
        objectInstance.Email = email
        objectInstance.Phone = phone
        objectInstance.Address = address
        objectInstance.Issue = issue
        objectInstance.save()
        subject = 'There is a query'
        message = f'Hi admin, There\'s a query from {name} please check the admin panel for more.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ["ljindal275@gmail.com", ]
        send_mail(subject, message, email_from, recipient_list)
    return render(request, 'contact/contact.html')
