'''
Created on 2018年7月13日

@author: Administrator
'''
from django.urls import path
from apps.ApiManager import views_api


urlpatterns = [
    path(r'get_project/', views_api.get_project, name='get_project'),
    path(r'get_module/', views_api.get_module, name='get_module'),
    path(r'Save_ApiInfo/', views_api.Save_ApiInfo, name='Save_ApiInfo'),
    path(r'Save_ApiHeader/',views_api.Save_ApiHeader,name='Save_ApiHeader')
]