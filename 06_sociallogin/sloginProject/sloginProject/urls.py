from django.contrib import admin
from django.urls import path, include
import loginApp.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(loginApp.urls)),
    path('accounts/', include('allauth.urls')),
]
