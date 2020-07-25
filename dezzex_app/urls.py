from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('signup',Signup.as_view(),name='signup'),
]