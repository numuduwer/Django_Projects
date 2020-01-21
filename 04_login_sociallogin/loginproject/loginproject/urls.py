from django.contrib import admin
from django.urls import path, include
import login.views
import sociallogin.views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sociallogin.views.home),
    path('accounts/', include('login.urls')),
    path('accounts/', include('allauth.urls')),
    
]


