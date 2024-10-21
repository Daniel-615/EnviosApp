from django.urls import path
from django.urls import include
urlpatterns = [
    path('app/',include('envios_app.urls'))
]
