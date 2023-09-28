from django import forms

class AddMemory(forms.Form):
    topic = forms.CharField()
    date = forms.DateField()