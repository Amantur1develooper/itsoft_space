from django.contrib import admin
from django.urls import path, include, re_path
from .views import *
from xml.etree.ElementInclude import include
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings 
#from django.conf.urls import url
urlpatterns = [
    path('', index, name='index' ),
    path('contact', contact, name='contact' ),
    path('our-services', service, name='service' ),
    path('about', about_us, name='about'),
    path('cource', cource, name='cource'),

]

# handler404 = "app.views.handler500"
# handler404 = "app.views.handler404"



# if settings.DEBUG:
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)