from django.db import models
from django.contrib.auth.models import User
# from froala_editor.fields import FroalaField
from ckeditor_uploader.fields import RichTextUploadingField

class TextField(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    # totalMail = models.IntegerField(default=0)
    # # content = FroalaField()
    text = RichTextUploadingField()



class SentData(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    totalsent = models.CharField(default=0,max_length=500000 , null=True)
    failed = models.CharField(default=0,max_length=500000,null=True)
    date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return (str(self.user))


class Count(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    count = models.IntegerField(default=0)
    updated_value = models.IntegerField(default=0,null=True)

    def __str__(self):
        return (str(self.user))
    
