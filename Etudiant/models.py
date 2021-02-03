'''
Created on 3 févr. 2021

@author: Enric Franck
'''
from django.db import models

class Member(models.Model):
    numero = models.CharField(max_length=10)
    nom = models.CharField(max_length=40)
    prenom = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    adresse = models.CharField(max_length=40)

    def __str__(self):
        return self.numero + " " + self.nom+ " " + self.prenom + " " + self.email+ " " + self.adresse