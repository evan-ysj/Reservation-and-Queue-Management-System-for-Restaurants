from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label="User Name", 
                               max_length=128, 
                               widget=forms.TextInput(attrs = {'class': 'form-control'}))
    password = forms.CharField(label="Password", 
                               max_length=256, 
                               widget=forms.PasswordInput(attrs = {'class': 'form-control'}))
    
    
class RegisterForm(forms.Form):
    username = forms.CharField(label="User Name", 
                               max_length=128, 
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Password", 
                                max_length=256, 
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirm Password", 
                                max_length=256, 
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email Address", 
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))