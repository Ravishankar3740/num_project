
from django.urls import path
from . import views
urlpatterns = [
    path('',views.homepage,name='home'),
    path('take_data/',views.take_data,name='data')
]