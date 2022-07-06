from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('addsign/', views.addsign, name = 'addsign'),
    path('search/', views.searchBar, name = 'search'),
    path('runModel/', views.runModel, name = 'runModel'),

]