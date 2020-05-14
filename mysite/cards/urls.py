from django.urls import path
from cards import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('fill/', views.fill_cards, name='fill_cards'),
    path('view_settings/', views.view_settings, name='view_settings'),
]
