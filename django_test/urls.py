
from django.contrib import admin
from django.urls import path,include
from .import views
from django.conf.urls.static import static
from django.conf import settings 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('front.urls')),
    path('', include('contact.urls')),
    path('', include('service.urls')),
   
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
