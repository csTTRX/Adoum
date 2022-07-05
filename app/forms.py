from django import forms
from .models import *

class FormationForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(
                attrs={'class':'text-input',
                'palceholder':'Nom de la formation'}))
    description = forms.CharField(widget=forms.Textarea(
                attrs={'class':'text-area',
                'palceholder':'Description de la formation'}))

    start_at = forms.DateField(widget=forms.DateInput(
                attrs={'class':'date-input', 
                'type':"date",
                'palceholder':'Date de debut'}))
    
    end_at = forms.DateField(widget=forms.DateInput(
                attrs={'class':'date-input', 
                'type':"date",
                'palceholder':'Date de fin'}))

    class Meta:
        model = Formations
        fields ="__all__"

class ExperienceForm(forms.ModelForm):

    type = forms.CharField(widget=forms.TextInput(
                attrs={'class':'text-input',
                'placeholder':"type d'experience (stage,..)"}))

    post = forms.CharField(widget=forms.TextInput(
                attrs={'class':'text-input',
                'placeholder':'Le post occupé'}))

    etablisment_name = forms.CharField(widget=forms.TextInput(
                attrs={'class':'text-input',
                'placeholder':"Nom de l'etablisement"}))

    description = forms.CharField(widget=forms.Textarea(
                attrs={'class':'text-area',
                'placeholder':'Description de la formation'}))

    start_at = forms.DateField(widget=forms.DateInput(
                attrs={'class':'date-input', 
                'type':"date",
                'placeholder':'Date de debut'}))
    
    end_at = forms.DateField(widget=forms.DateInput(
                attrs={'class':'date-input', 
                'type':"date",
                'palceholder':'Date de fin'}))
    class Meta:
        model = Experiences
        fields ="__all__"
    
class ContactForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(
                attrs={'class':'text-input',
                'placeholder':'Nom Complet'}))

    email  = forms.EmailField(widget=forms.EmailInput(
                attrs={'class':'text-input',
                'placeholder':'Email'}))

    message = forms.CharField(widget=forms.Textarea(
                attrs={'class':'text-area',
                'placeholder':'Votre message'}))
    class Meta:
        model = Contact
        fields = '__all__'