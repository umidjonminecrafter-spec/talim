from django.urls import path
from .views import (
    SmsTemplatesViewSet,
    SmsSchedulesViewSet,
    SMSMessagesViewSet, SmsProviderViewSet
)

urlpatterns = [
    path(
        'sms-templates/',
        SmsTemplatesViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='smstemplates-list'
    ),
    path(
        'sms-templates/<int:pk>/',
        SmsTemplatesViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }),
        name='smstemplates-detail'
    ),

    path(
        'sms-schedules/',
        SmsSchedulesViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='smsschedules-list'
    ),
    path(
        'sms-schedules/<int:pk>/',
        SmsSchedulesViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }),
        name='smsschedules-detail'
    ),


    path(
        'sms-messages/',
        SMSMessagesViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='smsmessages-list'
    ),
    path(
        'sms-messages/<int:pk>/',
        SMSMessagesViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }),
        name='smsmessages-detail'
    ),
    path('schedules/', SmsSchedulesViewSet.as_view({'get': 'list', 'post': 'create'}), name='sms-schedule-list'),
    path('schedules/<int:pk>/', SmsSchedulesViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='sms-schedule-detail'),

    path('providers/', SmsProviderViewSet.as_view({'get': 'list', 'post': 'create'}), name='sms-provider-list'),
    path('providers/<int:pk>/', SmsProviderViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='sms-provider-detail'),
]


