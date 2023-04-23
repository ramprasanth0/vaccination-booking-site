from django.urls import path
from User import views

# app_name='user_app'

#add url paths here
urlpatterns = [
    # path('user',views.user_booking,name='user')
    path('',views.user_booking),
    path('user_logout/',views.user_logout,name='user_logout'),
    #path('slot_booked/')
]
