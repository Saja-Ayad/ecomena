from operator import concat
from django import forms


from django import forms
from .models import Contact

class contactform(forms.ModelForm):
    class Meta:
        model= Contact
        fields= ["name", "email","subject"]