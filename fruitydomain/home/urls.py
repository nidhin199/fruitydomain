from django.urls import path
from. import views


urlpatterns = [
    path('', views.index),
    path('xyz/',views.test),
    path('login/',views.login,name='loginpage'),
    path('register/',views.register,name='registerpage'),
    path('logout/',views.logout),

]