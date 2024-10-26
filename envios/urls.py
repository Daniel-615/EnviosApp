from django.urls import path
from django.urls import include
from .views import home
urlpatterns = [
    path('app/',include('envios_app.urls')),
    path('',home,name='home_main')
]
