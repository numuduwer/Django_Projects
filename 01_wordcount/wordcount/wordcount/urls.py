from django.contrib import admin
from django.urls import path
import wordcountApp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', wordcountApp.views.home, name = 'home'),
    path('about/', wordcountApp.views.about, name = 'about'),
    path('result/', wordcountApp.views.result, name = 'result'),
]
