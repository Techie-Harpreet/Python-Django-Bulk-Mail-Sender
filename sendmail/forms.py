from django import forms
# from froala_editor.widgets import FroalaEditor
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *
from ckeditor.fields import RichTextFormField


# class YourModelForm(forms.ModelForm):
#     content = RichTextFormField(required=False)

class EmailForm(forms.ModelForm):
  text = forms.CharField(widget=CKEditorUploadingWidget(),required=False)
  class Meta:
    model = TextField
    fields = ['text']
    