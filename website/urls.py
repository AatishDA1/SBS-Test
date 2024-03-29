from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('member_zone', views.member_zone, name='member_zone'),
    path('available_datasets', views.available_datasets, name='available_datasets'),
]
