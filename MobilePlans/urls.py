from django.urls import path
from . import views

app_name = 'MobileRecharge'
urlpatterns = [
    path('', views.index, name='index')

]
