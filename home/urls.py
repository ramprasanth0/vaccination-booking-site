from django.urls import path
from . import views

#add url paths here
urlpatterns = [
    path('',views.home_page,name='home_page'),
    path('user_page/',views.user_page,name='user_page'),
    path('admin_page/',views.admin_page,name='admin_page'),
    path('sign_up/',views.sign_up,name='sign_up'),
    path('user_login_page/',views.user_login_page,name='user_login_page'),
    path('admin_login/',views.admin_login,name='admin_login'),
    #path('signup_error',views.signup_error,name='signup_error'),
]
