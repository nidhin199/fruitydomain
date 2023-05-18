from django.urls import path
from. import views

urlpatterns = [
    path('',views.about,name='prod'),
    path('cmt/',views.cmt),
    path('like/',views.like),
    path('autoc/',views.autoc,name='jauto'),
    path('about2/',views.about2)
    
]