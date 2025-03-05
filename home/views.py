from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from smtp.models import SmtpBackend
from sendmail.models import *
from accounts.models import User_Profile_Picture
from django.core.exceptions import ObjectDoesNotExist

def Home(request):
    # return render(request, 'home/index.html')
    return redirect('accounts/login')
    
@login_required(login_url='/accounts/login')
def Deashboard(request):
    smtpedit = SmtpBackend.objects.filter(user=request.user)
    totalmail = SentData.objects.filter(user=request.user)
    totalmailcount = Count.objects.filter(user=request.user)
    try:
        profile_picture = User_Profile_Picture.objects.get(user_id = request.user)
    except ObjectDoesNotExist:
        profile_picture = None  # Set to None if not found
    context = {
        'smtpedit': smtpedit,
        'totalmail' : totalmail,
        'totalmailcount' : totalmailcount,
        'profile_picture': profile_picture
    }
    return render(request, 'user dashboard/pages/dashboard.html', context)
