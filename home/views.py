from django.shortcuts import render
from .models import Service
from .models import Team
from home import views


# Create your views here.
def home(request):
    return render(request, "home/index.html", {'nbar':'home'})

def about(request):
     teams = Team.objects.all()

     return render(request, "home/about-us.html", {'teams':teams})

def services(request):
    services = Service.objects.all()

    return render(request, "home/services.html", {'services':services})

def contact(request):
    return render(request, "home/contact.html", {'nbar':'contact'})

def research(request):
    return render(request, "home/research.html", {'nbar':'research'})

def single_project(request):
    return render(request, "home/single_project.html")

def single_service(request, id):

    object_list = Service.objects.all() 
    instance = Service.objects.filter(id = id)
    print(instance)
    context = {
        'service': instance[0],
        'services': object_list
    }
    return render(request, "home/single_service.html", context)

def team_details(request, id):

    object_list = Team.objects.all() 
    instance = Team.objects.filter(id = id)
    print(instance)
    context = {
        'team': instance[0],
        'teams': object_list
    }
    return render(request, "home/team_details.html", context)



