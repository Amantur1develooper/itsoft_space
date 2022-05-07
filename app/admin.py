# from socket import AF_AAL5
from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
# Register your models here.


class LudiAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'phone','cource1','cource2','cource3','cource4', 'email', 'letter','created_at']
admin.site.register(Ludi, LudiAdmin)

class ImgAdmin(admin.ModelAdmin):
    list_display = ['id', 'title1',]
admin.site.register(Img, ImgAdmin)


class LinkAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'title1','link']
admin.site.register(Link, LinkAdmin)


class WorkersAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_', 'f_name', 'post','contact']

    def image_(self,obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))

    image_.__name__ = ""

    
admin.site.register(Workers, WorkersAdmin)


class ClientsAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'phone','cource1','cource2','cource3','cource4', 'email', 'letter','created_at']
admin.site.register(Clients, ClientsAdmin)