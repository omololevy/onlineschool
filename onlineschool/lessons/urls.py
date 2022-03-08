from django.urls import path
from .views import (SinfDetail, SinfList, FanList, FanDetail)

urlpatterns = [
    path('sinf/detail/<int:pk>', SinfDetail.as_view(), name='sinf_detail'),
    path('sinf/list', SinfList.as_view(), name='sinf_list'),
    path('fan/list', FanList.as_view(), name='fan_list'),
    path('fan/detail/<int:pk>', FanDetail.as_view(), name='fan_detail')
]