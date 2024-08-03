from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from .validator import CustomPasswordValidator
from .models import Account


def default_profile_image_path():
    return 'default_profile/default_profile.png'

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=30, required=True)
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = Account
        fields = ('email', 'username', 'password1', 'password2', 'profile_picture')

     #to prevent model validation
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data   

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Account.objects.filter(email=email).exists():
            raise forms.ValidationError("An user with that Email already exists.")
        email_validator=EmailValidator(message="Enter a valid email address.")
        try: 
            email_validator(email)
            print("good email")
        except ValidationError:
            print("yes bad email")
            raise forms.ValidationError("Bad Email Address.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username)<5:
            raise forms.ValidationError("Username is Too Short")
        elif Account.objects.filter(username=username).exists():
            raise forms.ValidationError("This username already Taken.")
        else:
            return username
        
    def clean_password1(self):
        password1=self.cleaned_data['password1']
        validator=CustomPasswordValidator()
        validator.validate(password1)
        return password1
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            print(password1 and password2 and password1 != password2)
            raise forms.ValidationError("Passwords didn't match.")
        return cleaned_data

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']
        #user.profile_picture = self.cleaned_data['profile_picture']
            # Check if profile_picture is provided, otherwise set default
        if self.cleaned_data.get('profile_picture'):
            user.profile_picture = self.cleaned_data['profile_picture']
            print("User provided a profile picture")
        else:
            user.profile_picture = default_profile_image_path()
            print("Default profile picture used")

        if commit:
            user.save()
        return user

    


