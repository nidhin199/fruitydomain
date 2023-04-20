from django.urls import path
from. import views


urlpatterns = [
    path('', views.index),
    path('xyz/',views.test),
    path('login/',views.login),
    path('login/loginsub/',views.loginsub),
    path('register/',views.register),
    path('register/registersub/',views.registersub),

]