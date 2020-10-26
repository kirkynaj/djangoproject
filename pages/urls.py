from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('about-us/', views.about, name='about'),
    path('enrollment-list/', views.enrollment, name='enrollment'),

]
