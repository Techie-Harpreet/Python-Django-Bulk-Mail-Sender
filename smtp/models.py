from django.db import models
from django.contrib.auth.models import User
import uuid

class SmtpBackend(models.Model):
    sid = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False) 
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    EMAIL_HOST = models.CharField(max_length=1000)
    EMAIL_HOST_USER = models.CharField(max_length=1000)
    EMAIL_HOST_PASSWORD = models.CharField(max_length=1000)
    EMAIL_PORT = models.CharField(max_length=1000)
    EMAIL_USE_TLS = models.CharField(max_length=1000)

    def __str__(self):
        return (str(self.user))