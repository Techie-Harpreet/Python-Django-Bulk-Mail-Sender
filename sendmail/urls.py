from .views import *
from django.urls import path,include
urlpatterns = [

    path("single-mail",Single_mail_send,name="Single_mail_send"),
    path("bulk-mail",Bulk_mail_send,name="Bulk_mail")



]