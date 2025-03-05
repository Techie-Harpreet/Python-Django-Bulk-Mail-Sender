from .views import *
from django.urls import path,include
urlpatterns = [

    path('register' , register_page ,name="register_page"),
    path('login', login_page, name="login_page"),
    path('logout', Logout, name="Logout"),
    path('profile', Profile, name="profile"),
    path('profile/update', Profile_Update, name="profile_update"),

]