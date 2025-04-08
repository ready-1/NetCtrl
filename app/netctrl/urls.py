"""
URL configuration for netctrl project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    # Admin URL
    path("admin/", admin.site.urls),
    
    # CMS URLs - will be defined in cms/urls.py
    path("cms/", include("cms.urls")),
    
    # Network app URLs - will be defined in network/urls.py
    path("network/", include("network.urls")),
    
    # Redirect root URL to CMS dashboard
    path("", RedirectView.as_view(url="/cms/dashboard/", permanent=False)),
    
    # User authentication URLs
    path("accounts/", include("django.contrib.auth.urls")),
]

# Serve media and static files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
