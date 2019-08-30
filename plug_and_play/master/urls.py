from django.urls import path,include

from . import views

app_name = 'master'
urlpatterns = [
    path('', views.index, name='index'),
    path('uploadjob/', views.uploadjob, name='uploadjob'),
    path('checkresult/', views.checkresult, name='checkresult'),
    path('storeresult/', views.storeresult, name='storeresult'),
]