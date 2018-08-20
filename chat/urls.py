from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^chat/$', views.index, name='index'),
    url(r'^chat/(?P<room_name>[^/]+)/$', views.room, name='room'),
    path('log/', views.log_index, name='log_index'),
    # url(r'^log/$',views.log_create, name='log_create'),
]