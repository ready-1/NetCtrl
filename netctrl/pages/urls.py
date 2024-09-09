from django.urls import path
from . import views

urlpatterns = [
    path("", views.pages, name="home"),
    path("pages/create/", views.create, name="create"),
    path("pages/edit/<slug:slug>/", views.edit, name="edit"),
    path("pages/delete/<slug:slug>/", views.delete, name="delete"),
    path("pages/<slug:slug>/", views.page, name="page"),
    path("pages/", views.pages, name="pages"),
]
