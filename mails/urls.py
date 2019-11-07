from django.urls import path
from . import views

app_name = 'mails'
urlpatterns = [
    path('',views.my_mails, name='myMail' ),
    path('send-mail',views.sendMail, name='sendMail' ),
]