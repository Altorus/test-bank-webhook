
from django.contrib import admin
from django.urls import path, include
from api import routers as api_routers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_routers)),
]
