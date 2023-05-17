from django.urls import path
from. import views
from.feed import latest

urlpatterns = [
    path('', views.index,name='homepage'),
    path('xyz/',views.test),
    path('login/',views.login,name='loginpage'),
    path('register/',views.register,name='registerpage'),
    path('logout/',views.logout),
    path('feed/',latest()),
    path('search/searchsub/',views.test),
    path('search/',views.search)
]