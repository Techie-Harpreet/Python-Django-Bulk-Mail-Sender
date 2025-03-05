from .views import *
from django.urls import path

urlpatterns = [
    path('' ,Home , name="Home"),
    path('dashboard' ,Deashboard , name="Deashboard"),

]