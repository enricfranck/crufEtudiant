'''
Created on 3 févr. 2021

@author: Enric Franck
'''
from django import forms
from Etudiant.models import Name

class NameForme(forms.ModelForm):
    name_value = forms.CharField(max_length=100)
    
    class Meta:
        model = Name
        fields=('name_value',)