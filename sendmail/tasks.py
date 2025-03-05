from celery import shared_task
from django.core.mail import EmailMessage, get_connection
from .models import SentData, Count
from smtp.models import SmtpBackend
from django.db.models import Sum
import os
from django.conf import settings
import pandas as pd

@shared_task
def bulk_mail_send_task(user_id, filename, subject, content, attachment_paths):
    try:
        # ✅ Read CSV/Excel file
        file_path = os.path.join(settings.MEDIA_ROOT, filename)
        try:
            data = pd.read_csv(file_path)
        except:
            data = pd.read_excel(file_path)

        emails = list(data['Emails'])

        # ✅ SMTP Details Fetch
        smtp_data = SmtpBackend.objects.get(user_id=user_id)
        connection = get_connection(
            host=smtp_data.EMAIL_HOST.strip(),
            port=smtp_data.EMAIL_PORT,
            username=smtp_data.EMAIL_HOST_USER,
            password=smtp_data.EMAIL_HOST_PASSWORD,
            use_ssl=smtp_data.EMAIL_USE_TLS,
        )

        # ✅ Save Sent Data
        sent_record = SentData(name=filename, totalsent=len(emails), user_id=user_id)
        sent_record.save()

        # ✅ Update Count
        Count.objects.create(count=len(emails), user_id=user_id)
        total_count = Count.objects.filter(user_id=user_id).aggregate(Sum('count'))['count__sum']
        Count.objects.create(updated_value=total_count, user_id=user_id)

        # ✅ Send Emails
        for email in emails:
            mail = EmailMessage(subject, content, smtp_data.EMAIL_HOST_USER, [email], connection=connection)

            # ✅ Attach Files
            for file_path in attachment_paths:
                with open(file_path, "rb") as f:
                    mail.attach(os.path.basename(file_path), f.read())

            mail.content_subtype = 'html'
            mail.send()

        return f"✅ Bulk mail task completed for {len(emails)} emails."

    except Exception as e:
        return f"❌ Error in bulk mail task: {str(e)}"
    
@shared_task
def Single_mail_send_task(user_id, email_list, subject, mail_content, attachments=None):
    counter = len(email_list)
    
    # Save email sending info
    s = SentData(name=email_list, totalsent=counter, user_id=user_id)
    s.save()

    countdata = Count(count=counter, user_id=user_id)
    countdata.save()

    # Calculate total count
    total_count = Count.objects.filter(user_id=user_id).aggregate(Sum('count'))['count__sum']

    updated_count_data = Count(updated_value=total_count, user_id=user_id)
    updated_count_data.save()

    # Get SMTP credentials
    smtp = SmtpBackend.objects.get(user_id=user_id)

    connection = get_connection(
        host=smtp.EMAIL_HOST.strip(),
        port=smtp.EMAIL_PORT,
        username=smtp.EMAIL_HOST_USER,
        password=smtp.EMAIL_HOST_PASSWORD,
        use_ssl=smtp.EMAIL_USE_TLS
    )

    # Send Emails with Attachments
    for email in email_list:
        mail = EmailMessage(subject, mail_content, smtp.EMAIL_HOST_USER, [email], connection=connection)
        mail.content_subtype = 'html'

        # Add Attachments (if available)
        if attachments:
            for file_path in attachments:
                with open(file_path, "rb") as f:
                    mail.attach(os.path.basename(file_path), f.read())

        mail.send()

    # Delete temporary attachment files after sending
    if attachments:
        for file_path in attachments:
            if os.path.exists(file_path):
                os.remove(file_path)

    return f"Emails Sent Successfully to {len(email_list)} recipients."