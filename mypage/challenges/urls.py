from django.urls import path
from . import views

urlpatterns = [
    path(""), #/challenges/ THIS IS THE INDEX OR HOME PAGE URL, THIS WORKS BY NOT TYPING ANTHING FURTHER INTO THE PROJECT!
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge")
]