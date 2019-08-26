from django.urls import path,include

from . import views

app_name = 'master'
urlpatterns = [
    path('', views.index, name='index'),
    path('uploadjob/', views.uploadjob, name='uploadjob'),
    path('addtext/', views.addtext, name='addtext'),
]