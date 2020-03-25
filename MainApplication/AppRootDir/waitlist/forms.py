from django import forms

class TakenoForm(forms.Form):
    no_of_guests = forms.IntegerField(label="Number of Guests", 
                                      widget=forms.TextInput(attrs = {'class': 'form-control',
                                                                      'placeholder':'Range: 0-10'}))
    name = forms.CharField(label="Last Name", 
                           max_length=128, 
                           widget=forms.TextInput(attrs = {'class': 'form-control',
                                                           'placeholder':'Please input your last name'}))

class CheckstateForm(forms.Form):
    number = forms.CharField(label="Wait List Number", 
                           max_length=128, 
                           widget=forms.TextInput(attrs = {'class': 'form-control',
                                                           'placeholder':'Please input your number',
                                                           'style': 'text-align: center;'}))
