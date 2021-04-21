from django.urls import path
from . import views

urlpatterns = [
   	
   	path('',views.homebase,name = 'homebase'),
    path('homepage/',views.homepage,name = 'homepage'),
    path('about/',views.about,name = 'about'),
    path('user_about/',views.user_about,name = 'user_about'),
    path('user_contact/',views.user_contact,name = 'user_contact'),
    path('contact/',views.contact,name = 'contact'),
    path('register/',views.register_person,name = 'register_person'),
    path('login/',views.login_person,name = 'login'),
    path('logout/',views.logout_person,name = 'logout'),
    path('search/',views.search,name = 'search'),
    path('admin_login/',views.admin_login,name = 'admin_login'),
    path('location/',views.location,name = 'location'),
]
