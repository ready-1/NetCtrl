from django.urls import path
from . import views

app_name = 'cms'

urlpatterns = [
    path('', views.file_manager, name='file_manager'),
    path('upload/', views.upload_file, name='upload'),
    path('create-folder/', views.create_folder, name='create_folder'),
    path('rename/', views.rename_item, name='rename'),
    path('delete/', views.delete_item, name='delete'),
    path('move/', views.move_item, name='move'),
    path('tags/add/', views.add_tag, name='add_tag'),
    path('tags/remove/', views.remove_tag, name='remove_tag'),
    path('tags/', views.get_tags, name='get_tags'),
    path('tags/filter/', views.filter_by_tags, name='filter_by_tags'),
]
