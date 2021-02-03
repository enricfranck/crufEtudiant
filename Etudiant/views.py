'''
Created on 3 févr. 2021

@author: Enric Franck
'''
from django.shortcuts import render, redirect

from Etudiant.models import Member


def index(request):
    members = Member.objects.all()
    context = {'members': members}
    return render(request, 'index.html', context)

def create(request):
    member = Member(numero=request.POST['numero'], nom=request.POST['nom'],
                    prenom=request.POST['prenom'], email=request.POST['email'],
                    adresse=request.POST['adresse'])
    member.save()
    return redirect('/')

def edit(request, id):
    members = Member.objects.get(id=id)
    context = {'members': members}
    return render(request, 'edit.html', context)

def update(request, id):
    member = Member.objects.get(id=id)
    member.numero = request.POST['numero']
    member.nom = request.POST['nom']
    member.prenom = request.POST['prenom']
    member.email = request.POST['email']
    member.adresse = request.POST['adresse']
    member.save()
    return redirect('/')

def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    return redirect('/')


