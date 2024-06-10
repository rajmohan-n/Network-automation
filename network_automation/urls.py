from django.urls import path
from  . import views



urlpatterns = [
    path('',views.home),
    path('devices',views.devices),
    path('configure',views.configure),
    path('verify_config',views.verify_config),
    path('logs',views.log)
]
