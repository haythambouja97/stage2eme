from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('compte',views.compte, name='compte'),
    path('recherche',views.recherche,name='recherche'),
    path('whoweare',views.whoweare,name='whoweare'),

    

]