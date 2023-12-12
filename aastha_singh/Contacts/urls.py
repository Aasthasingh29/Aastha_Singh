from django.urls import path

from .views import *

urlpatterns = [
    path('',index,name="HomePage"),
    path('create',create_contact_view,  name="Create"),
    path('view',list_view,  name="ListView"),
    path('<id>',detail_view,  name="DetailView"),
    path('<id>/update',update_view,  name="Update"),
    path('<id>/delete', delete_view,  name="Delete"),
]