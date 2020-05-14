from django.urls import path
from django.conf.urls import url
from cards import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('cards_list/', views.cards_list, name='cards_list'),
]
