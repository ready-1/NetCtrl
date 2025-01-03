"""
URL configuration for ctrl project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls), # Include the admin site
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'), # Use the built-in login view
    path('accounts/', include('accounts.urls')), # Include the accounts app's URLs
    path('net_frontend/', include('net_frontend.urls')),  # Include the net_frontend app's URLs
    path('wiki/', include('wiki.urls')),  # Include the wiki app's URLs
    path('bugtracker/', include('bugtracker.urls')),  # Include the bugtracker app's URLs
    path('', lambda request: redirect('wiki:wiki_list', permanent=False)),  # Redirect "/" to wiki_list
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)