from django.urls import path
from . import views

app_name = 'wiki'  # This is the namespace for the app

urlpatterns = [
    path('', views.wiki_list, name='wiki_list'),
    path('page/<int:pk>/', views.wiki_detail, name='wiki_detail'),
    path('add/', views.wiki_add, name='wiki_add'),
    path('edit/<int:pk>/', views.wiki_edit, name='wiki_edit'),
    path('delete/<int:pk>/', views.wiki_delete, name='wiki_delete'),
]