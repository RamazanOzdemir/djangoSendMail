from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

def my_mails(request):
    return render(request,'mails/my_mail.html')


def sendMail(request):
    send_mail('ilk', 'django ile ikinci mesaj','dene6606@gmail.com', 
    ['dene666666@gmail.com'],fail_silently=False, auth_user='dene6606@gmail.com', auth_password='Kartal1903')
    return render(request,'mails/my_mail.html')