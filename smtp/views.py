from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from accounts.models import User_Profile_Picture
from django.core.exceptions import ObjectDoesNotExist

def SMTPEdit(request, id):
    s = SmtpBackend.objects.get(sid=id)
    print(s)
    smtpedit = SmtpBackend.objects.filter(user=request.user)
    profile_picture = User_Profile_Picture.objects.get(user_id = request.user)

    context = {
        'smtpedit': smtpedit,
        's' : s,
        'profile_picture' : profile_picture
    }
    if s.user != request.user:
        return redirect('/register')

    return render(request, 'user dashboard/pages/smtp-edit.html', context)

def SMTPupdate(request, id):
    if request.method == "POST":
        s = SmtpBackend.objects.get(sid=id)
        print(s)
        if s.user != request.user:
            return redirect('/register')

        ehost = request.POST['ehost']
        ehostuser = request.POST['ehostuser']
        ehost = request.POST['ehost']
        epass = request.POST['epass']
        eport = request.POST['eport']
        etls = request.POST['etls']

        s.EMAIL_HOST = ehost
        s.EMAIL_HOST_USER = ehostuser
        s.EMAIL_HOST_PASSWORD = epass
        s.EMAIL_PORT = eport
        s.EMAIL_USE_TLS = etls

        s.save()
        messages.success(request, 'updated successfully')

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


    return render(request, 'user dashboard/pages/smtp-edit.html', {'s': s})

def SMTPadd(request):
    smtpedit = SmtpBackend.objects.filter(user=request.user)
    try:
        profile_picture = User_Profile_Picture.objects.get(user_id = request.user)
    except ObjectDoesNotExist:
        profile_picture = None  

    context = {
        'smtpedit': smtpedit,
        'profile_picture' : profile_picture

    }

    if request.method == "POST":
        ehost = request.POST['ehost']
        ehostuser = request.POST['ehostuser']
        ehost = request.POST['ehost']
        epass = request.POST['epass']
        eport = request.POST['eport']
        etls = request.POST['etls']

        newdata = SmtpBackend(EMAIL_HOST=ehost, EMAIL_HOST_USER=ehostuser,
                            EMAIL_HOST_PASSWORD=epass, EMAIL_PORT=eport, EMAIL_USE_TLS=etls)
        newdata.user = request.user
        newdata.save()
        messages.success(request, 'Added Sucessfully')

        return redirect("/smtp/add")

    return render(request, 'user dashboard/pages/smtp-add.html',context)

def deleteSmtp(request,id):   
    s = SmtpBackend.objects.get(sid=id)
    if s.user != request.user:
        return redirect('/register')
    s.delete()
    messages.error(request, 'deleted successfully' , extra_tags='deletesmtp')

    return redirect('/smtp/add')





