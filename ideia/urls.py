from django.urls import path
from .views import *
urlpatterns = [
    path('listaIdeia/', ideialista, name="ideialista"),
    path('', ideia_create, name="ideiacreate"),
    path('deleteIdeia/<int:pk>', ideia_delete, name="Ideiadelete"),
    path('updateIdeia/<int:pk>', IdeiaUpdatea, name="Ideiaupdate"),

    ]