from django.urls import path
from django.conf.urls.i18n import i18n_patterns
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('menu/', Menu, name='menu'),
    path('reservation/', Reservation, name='reservation'),
    path('about/', About, name='about'),
    path('contact_us/', Contact_Us, name='contact_us'),

    path('register/', Register, name='register'),
    path('login/', Loginpage, name='login'),
    path('logout/', Logoutuser, name='logout'),

    path('create_menu/', createMenuItem, name='create_menu'),
    path('update_menu/<int:pk>', updateMenuItem, name='update_menu'),
    path('delete_menu/<int:pk>', deleteMenuItem, name='delete_menu'),

]