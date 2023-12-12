from django.urls import path

from .views import *

urlpatterns = [
    path('',index,name="HomePage"),
    path('create',create_contact_view, name="Create"),
]