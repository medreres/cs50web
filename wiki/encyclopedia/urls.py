from django.urls import path
from . import libr

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("add", views.add, name="add"),
    path("rand", views.rand, name="rand"),   
    path("<str:name>", views.page, name="page"),
    path("<str:name>/edit", views.edit, name="edit"),
      
]
