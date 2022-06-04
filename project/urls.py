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
admin.site.site_title = 'Project'
admin.site.index_title = 'Модерация сайта'

urlpatterns = [
    #django admin panel
    path('admin/', admin.site.urls),

    #index page
    path('', views.index),
    path('cart/', include('cart.urls', namespace='cart')),

    #Отображение страниц с товарами
    path('baked/',    views.baked),
    path('sushi/',    views.sushi),
    path('rolls/',    views.rolls),
    path('sets/',    views.sets),
    path('tempured/',    views.tempured),
    path('wok/',    views.wok),
    path('soup/',    views.soup),
    path('hotandsalads/',    views.hotandsalads),
    path('minirolls/',    views.minirolls),
    path('magrolls/',    views.magrolls),
    path('vegan/',    views.vegan),
    path('deserts/',    views.deserts),
    path('drinks/',    views.drinks),
    path('stuff/',    views.stuff),
    path('pizza/',    views.pizza),

    path('<int:id>/', views.ProductDetails.as_view(), name = 'product_details_url'),

   


    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
