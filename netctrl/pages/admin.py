from django.contrib import admin
from . import models

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')

admin.site.register(models.Page)