from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
path('', views.ytb_down, name='home'),
path('download/', views.yt_download),
path('download_complete/<res>', views.download_complete, name='download_complete'),

]
