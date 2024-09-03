from django.contrib import admin
from django.urls import path
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('mlsgrid.urls')),
    path('api/',include('mlsgrid.urls')),
    path('api/stellar/',include('stellarapp.urls')),
    path('auth/',include('authapp.urls'))
]
