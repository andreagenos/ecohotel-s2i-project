from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_data, name= 'show_data'),
    path('', views.staff_report, name='staff'),
    path('', views.record_data, name='record_data'),
]