from django import forms

class Encrypdata(forms.Form):
    Rawdata=forms.CharField()
    depth=forms.IntegerField()

class Decrypdata(forms.Form):
    Rawdata=forms.CharField()
    depth=forms.IntegerField()
