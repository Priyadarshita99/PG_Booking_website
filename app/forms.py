from app.models import *
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        help_texts={'username':''}
        widgets={'password':forms.PasswordInput}
     
class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['address','profile_pic']
        widgets={'address':forms.Textarea(attrs={'rows':3,'cols':40}),}

class PgForm(forms.ModelForm):
    class Meta():
        model=Pgs
        fields='__all__'
  
class BookingForm(forms.ModelForm):
    class Meta():
        model=Booking
        fields='__all__'
        widgets={'address':forms.Textarea(attrs={'rows':3,'cols':40}),}
