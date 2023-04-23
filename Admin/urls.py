from django.urls import path
from . import views

#add url paths here
urlpatterns = [
    path('',views.admin_access),
    path('admin_access',views.admin_access),
]
