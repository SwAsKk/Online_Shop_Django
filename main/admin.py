from django.contrib import admin
from .models import ClassicSet, BakedSet, ComboSet



# Register your models here.
admin.site.register(ClassicSet)
admin.site.register(BakedSet)
admin.site.register(ComboSet)