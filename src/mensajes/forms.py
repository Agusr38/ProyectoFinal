from django import forms

class MensajesForm(forms.Form):
    mensajes = forms.CharField(max_length=100)