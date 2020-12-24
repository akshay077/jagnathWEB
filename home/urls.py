from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('services', views.services, name="services"),
    path('contact', views.contact, name="contact"),
    path('research', views.research, name="research"),
    path('single_project', views.single_project, name="single_project"),
    path('single_service/<int:id>', views.single_service, name = "single_service"),
    path('team_details/<int:id>', views.team_details, name = "team_details"),

]