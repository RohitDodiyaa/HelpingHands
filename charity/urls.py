from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('causes/', views.causes, name='causes'),
    path('events/', views.events, name='events'),
    path('news/', views.news, name='news'),
    path('contact/', views.contact, name='contact'),
    path('donate/', views.donation_form, name='donation_form'),
    path('donate/confirmation/', views.donation_confirmation, name='donation_confirmation'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
]
