from django.contrib import admin
from django.urls import path, include
import functioncrud.urls
import functioncrud.views
import classcrud.views
import classcrud.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', functioncrud.views.welcome, name="welcome"),
    path('funccrud/', include(functioncrud.urls)),
    path('classcrud/', include(classcrud.urls)),
]
