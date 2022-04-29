"""
project URL Configuration
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from main import views

# Renaming django admin title
admin.site.site_header = 'Панель администрации'
admin.site.site_title = 'Project'
admin.site.index_title = 'Модерация сайта'

urlpatterns = [
    #django admin panel
    path('admin/', admin.site.urls),

    #index page
    path('', views.index),


    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
