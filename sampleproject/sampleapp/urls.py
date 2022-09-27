
from . import views
from django.urls import path

urlpatterns = [
    path('', views.demo, name='demo'),
    # path('login',views.login,name='login'),
    # path('logout', views.logout, name='logout'),
    # path('subtraction/', views.subtraction, name='subtraction'),
    # path('multiplication/', views.multiplication, name='multiplication'),
    # path('division/', views.division, name='division')
    # path('about/',views.about,name='about'),
    # path('contact/',views.contact,name='contact'),
    # path('details', views.details, name='details'),
    # path('thank', views.thank, name='thank')
]
