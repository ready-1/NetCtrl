from django.urls import path
from . import views

urlpatterns = [
    path("alert/<str:type>/", views.test_alert, name="test-alert"),
    path("buttons/", views.test_buttons, name="test-buttons"),
    path("card/", views.test_card, name="test-card"),
    path("loading/", views.test_loading, name="test-loading"),
    path("form/", views.test_form, name="test-form"),
    path("components/", views.test_components, name="test-components"),
]
