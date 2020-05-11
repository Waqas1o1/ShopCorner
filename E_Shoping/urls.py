from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static 
from . import views
urlpatterns = [
    path('',views.Index),
    path('admin/', admin.site.urls),
    path('Shop/',include('Shop.urls')),
    path('Blog/',include('Blog.urls')),
] + static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
