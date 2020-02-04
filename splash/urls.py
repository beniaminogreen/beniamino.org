from django.urls import path
from . import views

urlpatterns = [
        path('',views.home, name = "splash"),
        path('new',views.login, name = "new"),
        path('callback/',views.callback)
        ]
