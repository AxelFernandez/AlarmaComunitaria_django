from django.urls import path

from api.views import Registry, AlarmApi, PhoneAndAddress

urlpatterns = [
    path('registry', Registry.as_view(), name='registry'),
    path('send_alarm', AlarmApi.as_view(), name='alarm'),
    path('update_info', PhoneAndAddress.as_view(), name='update-info'),
]