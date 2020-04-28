
from django.contrib import admin
from django.urls import path
import xadmin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
]
