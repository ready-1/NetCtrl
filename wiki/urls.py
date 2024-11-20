from django.urls import path
from . import views

urlpatterns = [
    path('', views.wiki_list, name='wiki_list'),
]