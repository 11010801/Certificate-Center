from django import forms
class VerifyUsers(forms.Form):
    pubkey=forms.TextField()
