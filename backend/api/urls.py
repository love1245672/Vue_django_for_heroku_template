from django.urls import path
 
from . import views
 
urlpatterns = [
    path('show_all', views.show_all, name='show_all'),
]