
from django.contrib import admin
from django.urls import path, include
from ideia import urls as ideia_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(ideia_urls))
]