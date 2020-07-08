from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from myblog.models import User, Profile

class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

#added for the profile
class EditProfileForm(ModelForm):
    class Meta:
        model = User
        fields = (
                 'email',
                 'first_name',
                 'last_name'
                )
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('user', 'dob') #Note that we didn't mention user field here.
