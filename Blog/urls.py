from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls import static
urlpatterns = [
    path("", views.index, name="blogHome"),
    path("blogpost/<int:pid>/", views.blogpost, name="blogHome")
]