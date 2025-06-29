from django import forms

class BitwiseForm(forms.Form):
    a = forms.IntegerField(label='Enter the first number', min_value=0)
    b = forms.IntegerField(label='Enter the second number', min_value=0)
    c = forms.IntegerField(label='Enter the third number', min_value=0)
    d = forms.IntegerField(label='Enter the fourth number', min_value=0)
    e = forms.IntegerField(label='Enter the fifth number', min_value=0)