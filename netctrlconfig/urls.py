from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

# Customize admin site
admin.site.site_header = 'Network Control Administration'
admin.site.site_title = 'NetCtrl Admin'
admin.site.index_title = 'Network Control Management'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cli-manual/<path:filename>/', TemplateView.as_view(template_name='cli_manual.html'), name='view_cli_manual'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
