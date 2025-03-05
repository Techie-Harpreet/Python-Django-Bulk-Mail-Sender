from .views import *
from django.urls import path
urlpatterns = [

    path('edit/<uuid:id>', SMTPEdit , name="SmtpEdit"),  
    path('update/<uuid:id>', SMTPupdate , name="Notesupdate"),  
    path('add', SMTPadd , name="SMTPadd"),      
    path('delete-smtp/<uuid:id>', deleteSmtp,name="delete"), 


]