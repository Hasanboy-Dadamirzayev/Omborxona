
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('sell/', include('stats.urls')),
    path('auth/', include('users.urls')),
]
