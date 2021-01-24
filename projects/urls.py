from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_detail, name="home_detail"),
    path("projects/", views.project_index, name="project_index"),
    path("projects/<int:pk>/", views.project_detail, name="project_detail"),
    path("contact/", views.contact_detail, name="contact_detail"),


    
]