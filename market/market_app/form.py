from django import forms

# Create your forms here.

class ContactForm(forms.Form):
    fist_name = forms.CharField(max_length = 50)
    last_name = forms.CharField(max_length = 50)
    email_address = forms.EmailField(max_)