from django.contrib.auth.models import User
from django import forms
from django.core.validators import MinLengthValidator

class UserForm(forms.ModelForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), validators=[MinLengthValidator(11)])
    
    
    class Meta:
        model = User
        fields = ['username', 'password',]
