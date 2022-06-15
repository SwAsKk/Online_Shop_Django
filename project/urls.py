"""
    project URL Configuration
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from main import views

# Renaming django admin title
admin.site.site_header = 'Панель администрации'
admin.site.site_title = 'Sushiman'
admin.site.index_title = 'Модерация сайта'

urlpatterns = [
    # Django admin panel
    path('admin/', admin.site.urls),

    # Index page
    path('', views.index),

    # Cart pages
    path('cart/', include('cart.urls', namespace='cart')),
    path('adresses/', views.adresses),

    # Отображение страниц с товарами
    path(r'category/<slug:category_slug>/', views.view_category, name="main_category"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
