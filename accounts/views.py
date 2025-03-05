from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,  login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User_Profile_Picture
from smtp.models import SmtpBackend
from django.core.exceptions import ObjectDoesNotExist
from accounts.models import User_Profile_Picture  

def register_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username=email)
        if user_obj.exists():
            messages.warning(request, 'Email is already exist')
            return HttpResponseRedirect(request.path_info)

        # User Create Karo
        user_obj = User.objects.create(email=email, username=email)
        user_obj.set_password(password)
        user_obj.save()

        # Default Profile Picture Set Karo
        User_Profile_Picture.objects.create(
            user=user_obj, 
            avatar="User-Profile-Picture/default.jpg"
        )

        login(request, user_obj)
        return redirect('/dashboard')

    return render(request, 'accounts/register.html')


def login_page(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=email)

        if not user_obj.exists():
            messages.warning(
                request, 'Invalid email and password', extra_tags='login-error')

        user_obj = authenticate(username=email, password=password)
        if user_obj:
            login(request, user_obj)
            return redirect('/dashboard')

        return HttpResponseRedirect(request.path_info)
    return render(request, 'accounts/login.html')


def Logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/accounts/login')

@login_required(login_url='/accounts/login')
def Profile(request):
    try:
        profile_picture = User_Profile_Picture.objects.get(user_id = request.user)
    except ObjectDoesNotExist:
        profile_picture = None  
    smtpedit = SmtpBackend.objects.filter(user=request.user)

    context = {
        'smtpedit': smtpedit,
        'profile_picture' : profile_picture,
        
    }

    return render(request,"user dashboard/pages/profile.html",context)

@login_required(login_url='/login')
def Profile_Update(request):
    if request.method == "POST" :
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_id = request.user.id



        user = User.objects.get(id=user_id)
        user.username = username
        user.email = email


        if password != None and password != "":
            user.set_password(password)
        user.save()

        if 'p_picture' in request.FILES:
            # profile = User_Profile_Picture.objects.get(user_id = request.user)
            try:
                profile = User_Profile_Picture.objects.get(user_id = request.user)
            except ObjectDoesNotExist:
                profile = None  
            profile.avatar = request.FILES['p_picture']
            profile.save()
        messages.success(request,'Profile Are Successfully Updated')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
