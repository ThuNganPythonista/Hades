from src.public.apps.home.models import *
from django.contrib import admin
from src.public.apps.home.models import Items

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
        list_display = ['title','price','code','discount','color','description','size','categories']



class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['categories']

class ImgAdmin(admin.ModelAdmin):
        list_display = ['product','img']



admin.site.register(Items, ItemAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Img, ImgAdmin)