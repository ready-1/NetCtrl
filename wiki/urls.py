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

# File manager URLs
urlpatterns += [
    path('files/', views.file_list, name='file_list'),
    path('files/upload/', views.file_upload, name='file_upload'),
    path('files/<int:pk>/delete/', views.file_confirm_delete, name='file_confirm_delete'),
    path('image-upload/', views.image_upload, name='image_upload'),
    path('files/api/', views.file_list_api, name='file_list_api'),
]