from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='frases-home'),
    path('about/', views.about, name='frases-about'),
]