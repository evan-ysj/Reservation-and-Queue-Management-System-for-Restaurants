from django import forms

class ReservationForm(forms.Form):
    no_of_guests = forms.IntegerField(label="Number of Guests", 
                               widget=forms.TextInput(attrs = {'class': 'form-control',
                                                                'placeholder':'Range: 0-10'}))
    bookdate = forms.DateField(label="Pick a Date", 
                               widget=forms.DateInput(attrs = {'class': 'form-control',
                                                                'id': 'date_pick',
                                                                'placeholder':'Format: YYYY-MM-DD'}))