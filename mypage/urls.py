from django.urls import path
from . import (views)

urlpatterns = [
    path('',views.base,name='base'),
    path('/<slug:slug>/',views.detail,name='detail')
]
