from django.contrib import admin
from src.public.apps.home.models import *

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
        list_display = ['title','price','code','discount','color','description','size','categories']

class SizeAdmin(admin.ModelAdmin):
        list_display = ['size']


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['categories']

class ImgAdmin(admin.ModelAdmin):
        list_display = ['product','img']



admin.site.register(Items, ItemAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Img, ImgAdmin)