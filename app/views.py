from django.shortcuts import render
from app.models import Experiences, Formations
from .forms import ContactForm, FormationForm, ExperienceForm
from django.http.response import HttpResponse
# Create your views here.

def home(request):
    form = ContactForm()
    experiences = Experiences.objects.all()
    formations = Formations.objects.all()
    context = {'formations':formations,
                'experiences':experiences,
                'form':form,
                }
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Votre message a bien été envoyé, Merci!')
    return render(request, 'home.html', context)

def add_formation(request):
    form = FormationForm()
    if request.method == 'POST':
        form = FormationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'add_formation.html', context={'form':form})


def get_formations(request):
    return render('list_formation.html')

def del_formation(request, id):
    formation = Formations.objects.get(id=id)
    del_form = FormationForm(instance = formation)
    if request.method == 'POST':
        del_form = FormationForm(request.POST, instance = formation)
        formation.delete()
    return render(request, 'del_formation.html', context={'del_form': del_form})

def add_experience(request):

    form = ExperienceForm()
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'add_experience.html', context={'form':form})

def get_experiences(request):
    return render('list_experience.html')

def del_experience(request, id):
    experience = Experiences.objects.get(id=id)
    del_form = Experiences(instance = experience)
    if request.method == 'POST':
        del_form = FormationForm(request.POST, instance = experience)
        experience.delete()
    return render(request, 'del_experience.html', context={'del_form':del_form})