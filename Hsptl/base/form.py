from django import forms
from .models import *

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'}),
            'p_name':forms.TextInput(attrs={'placeholder':'enter your name'}),
            'p_phone':forms.NumberInput(attrs={'placeholder':'enter your number'}),
            'p_email':forms.EmailInput(attrs={'placeholder':'enter your mail'})
        }
        labels = {

        'p_name':'Patient name',
        'p_phone':'Patient number',
        'p_email':'Patient mail ',
        }