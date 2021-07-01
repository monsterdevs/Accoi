from django import forms
from .models import UserForm
# class StudentRegistration(forms.Form):
#     name=forms.CharField()
#     email=forms.EmailField()

class UserForm(forms.Form):
    Url = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form:control'
        }
    ),label=' Enter URL ')
    IP = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form.control'
        }
    ),label=' Enter IP ' )
    requestHeaders = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form.control'
        }
    ),label=' Enter Request Headers ')

    class Meta:
        model = UserForm

    fields = {'Url', 'IP', 'requestHeaders'}

# class UserForm(forms.ModelForm):
# UserName = forms.CharField(widget=forms.TextInput(
# attrs={
# 'class': 'form:control'
# }
# ), label='Enter Name')
# MobileNo = forms.IntegerField(widget=forms.TextInput(
# attrs={
# 'class': 'form:control'
# }
# ), label='enter your number')
# EmailId = forms.EmailField(widget=forms.TextInput(
# attrs={
# 'class': 'form:control'
# }
# ), label='enter email')

# class Meta:
# model = User
# fields = {'UserName', 'MobileNo', 'EmailId'}