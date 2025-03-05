from django.db import models
from django.contrib.auth.models import User

class User_Profile_Picture(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to='User-Profile-Picture'
        # default="C:/Harpreet-Personal/Personal-Projects\Django Bulk Mail/bulkmail/media/User-Profile-Picture/default.jpg"
    )

    def __str__(self):
        return self.user.username
