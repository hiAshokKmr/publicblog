
#Form

from django import forms
from .models import Post
from ckeditor.widgets import CKEditorWidget


class AuthenticatedPostCreateForm(forms.ModelForm):
    content = forms.CharField(widget = CKEditorWidget())
    class Meta:
        model = Post
        fields = ['title','category','language','content','thumbnail'] 
        
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title and len(title) < 50:
            raise forms.ValidationError("Title must be at least 50 characters long.")
        return title




class UnauthenticatedPostCreateForm(forms.ModelForm):
    name = forms.CharField(required=True, max_length=100)
    email = forms.EmailField(required=True)
    content = forms.CharField(widget = CKEditorWidget())
    class Meta:
        model = Post
        fields = ['title','category','language','content','thumbnail','name','email'] 

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Example: Check if email domain is from example.com
        if email and email.endswith("@example.com"):
            raise forms.ValidationError("Email addresses from example.com are not allowed.")
        return email

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 8:
            raise forms.ValidationError("Username must be at least 8 characters long.")
        return name
    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title and len(title) < 50:
            raise forms.ValidationError("Title must be at least 50 characters long.")
        return title




