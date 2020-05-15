from django.urls import path
from django.conf.urls import url
from choicess import views

urlpatterns = [
    path('', views.choicess_view, name='choicess_view'),
    path('qa', views.choicess_aq, name='qa'),

]
