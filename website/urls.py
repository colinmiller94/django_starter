from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='website-home'),
    path('resume/', views.resume, name='website-resume'),
    path('contact/', views.contact, name='website-contact'),
    path('calculator/', views.calculator, name='website-calculator'),
]
