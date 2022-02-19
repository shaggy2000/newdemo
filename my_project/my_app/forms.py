from django import forms

class UserForm(forms.Form):
    name = forms.CharField()
    email_address = forms.EmailField()
    roll_no = forms.CharField()
    feedback = forms.CharField(widget=forms.Textarea)
