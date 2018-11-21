#author_by zhuxiaoliang
#2018-11-06 下午2:49

from django.urls import path,re_path
from .views import reg,test,register,register2,index2,login2,logout,login3,ajax_login,alogin
app_name = 'user'

urlpatterns = [

    re_path(r'reg$',reg),
    path('test',test),
    path('register',register),
    path('register2',register2),
    path('index2/',index2),
    path('login2/',login2),
    path('logout/',logout),
    path('login3/',login3),
    path('ajax_login/',ajax_login),
    path('alogin/',alogin,name='alogin'),

]
