from django.urls import path,include
from .views import *
from . import views 

urlpatterns = [
    path('',views.home,name='home'),
    path('departments/',views.departments,name='departments'),
    path('booking/',views.booking,name='booking'),
    path('doctors/',views.doctors,name='doctors'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),

    path('docdetailview/<int:pk>',DocDetailView.as_view(),name='docdetailview')


]
