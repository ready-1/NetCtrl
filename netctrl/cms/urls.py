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
]
