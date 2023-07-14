from django.urls import path
from .import views


urlpatterns = [
    path('place_order/',views.place_order,name="place_order"),
    path('myorders/',views.myorders, name="myorders"),
    path('userprofile/',views.userProfile, name='user_profile')
]
