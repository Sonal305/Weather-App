from django import forms
from main.models import City

class CityForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'City Name'}))
    class Meta:
        model=City
        fields="__all__"
        #widgets={'name':TextInput(attrs={'class':'input','placeholder':'City Name'})}
