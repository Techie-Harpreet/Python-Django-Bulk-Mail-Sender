from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from smtp.models import SmtpBackend
from django.contrib import messages
from .models import *
from .forms import *
from django.conf import settings
from django.db.models import Sum
from accounts.models import User_Profile_Picture
from .tasks import Single_mail_send_task  , bulk_mail_send_task
import os
from django.core.exceptions import ObjectDoesNotExist

def replace_relatve_path_with_Absolute_url(request, message):
    search_pattern = settings.MEDIA_URL + settings.CKEDITOR_UPLOAD_PATH
    replace_with = request.build_absolute_uri(search_pattern)
    if __name__ == "sendmail.views":  # contact form mail App.views
        message = message.replace(search_pattern, replace_with)
        return message

@login_required(login_url='/login')
def Single_mail_send(request):
    smtpedit = SmtpBackend.objects.filter(user=request.user)
    try:
        profile_picture = User_Profile_Picture.objects.get(user_id = request.user)
    except ObjectDoesNotExist:
        profile_picture = None

    context = {
        'form': EmailForm,
        'smtpedit': smtpedit,
        'profile_picture': profile_picture
    }

    if request.method == "POST":
        form = EmailForm(request.POST)
        
        if form.is_valid():
            email_content = replace_relatve_path_with_Absolute_url(request, form.cleaned_data['text'])
            print("fdhsjfkjsdfkd",email_content)

        email = request.POST["email"]
        email_list = [e.strip() for e in email.split(',')]  
        subject = request.POST["subject"]
        user_id = request.user.id

        # ✅ Ensure the temp folder exists
        temp_folder = "media/temp_attachments"
        if not os.path.exists(temp_folder):
            os.makedirs(temp_folder)  # Create folder if not exists

        # ✅ Handle Attachments
        attachment_paths = []
        files = request.FILES.getlist("attach")
        for file in files:
            file_path = os.path.join(temp_folder, file.name)  
            with open(file_path, "wb") as f:
                f.write(file.read())
            attachment_paths.append(file_path)

        # ✅ Trigger Celery Task with Attachments
        Single_mail_send_task.delay(user_id, email_list, subject, email_content, attachment_paths)

        messages.success(request, 'Emails are being sent in the background.')
        return redirect(request.META.get('HTTP_REFERER', "/send-mail/single-mail"))

    return render(request, 'user dashboard/pages/send-single-mail.html', context)


@login_required(login_url='/login')
def Bulk_mail_send(request):
    smtpedit = SmtpBackend.objects.filter(user=request.user)
    try:
        profile_picture = User_Profile_Picture.objects.get(user_id = request.user)
    except ObjectDoesNotExist:
        profile_picture = None

    context = {
        'form': EmailForm,
        'smtpedit': smtpedit,
        'profile_picture': profile_picture
    }

    if request.method == "POST" and request.FILES.get('myfile'):
        form = EmailForm(request.POST)
        if form.is_valid():
            content = replace_relatve_path_with_Absolute_url(request, form.cleaned_data['text'])

        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)

        # ✅ Ensure the temp folder exists
        temp_folder = "media/temp_attachments"
        if not os.path.exists(temp_folder):
            os.makedirs(temp_folder)

        # ✅ Handle Attachments
        attachment_paths = []
        files = request.FILES.getlist("attach")
        for file in files:
            file_path = os.path.join(temp_folder, file.name)
            with open(file_path, "wb") as f:
                f.write(file.read())
            attachment_paths.append(file_path)

        # ✅ Trigger Celery Task
        bulk_mail_send_task.delay(request.user.id, filename, request.POST["subject"], content, attachment_paths)

        messages.success(request, 'Bulk emails are being sent in the background.')
        return redirect(request.META.get('HTTP_REFERER', "/send-mail/bulk-mail"))

    return render(request, 'user dashboard/pages/send-bulk-mail.html', context)