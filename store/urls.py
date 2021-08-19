from django.urls import path, include
from . import views

app_name = 'store'
urlpatterns = [
    path('', views.optimal_menu, name='optimal_menu')
]
