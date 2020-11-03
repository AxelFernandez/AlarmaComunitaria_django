import requests
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.base_user import BaseUserManager

from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Alarm, UserExtension


class Registry(APIView):

    def post(self, request):

        # create user if not exist
        is_completed_registred = False
        is_new = False
        try:
            user = User.objects.get(email=request.data.get('email'))
            extension = UserExtension.objects.filter(user=user)
            if len(extension) != 0:
                is_completed_registred = True



        except User.DoesNotExist:
            user = User()
            user.username = request.data.get('email')
            # provider random default password
            user.password = make_password(BaseUserManager().make_random_password())
            user.email = request.data.get('email')
            user.first_name = request.data.get('givenName')
            user.last_name = request.data.get('familyName')
            is_new = True
            user.save()
        if is_completed_registred:
            response = {"isNew": is_new,
                        "isCompletedRegistered": is_completed_registred,
                        "clientId": user.pk,
                        "username": user.username,
                        "phone": extension.get().phone,
                        "address": extension.get().address,
                        }
        else:
            response = {"isNew": is_new,
                    "isCompletedRegistered": is_completed_registred,
                    "clientId": user.pk,
                    "username": user.username,
                    }
        return Response(response)


class AlarmApi(APIView):

    def post(self, request):
        try:
            alarm_type = request.data.get("alarmType")
            location = request.data.get("location")
            user_id = request.data.get("userId")
            user = User.objects.get(pk=user_id)
            alarm = Alarm()
            alarm.user = user
            alarm.location = location
            alarm.alarm_type = alarm_type
            alarm.save()
            send_notification(alarm)
            return Response({"done": True})

        except Exception:
            return Response({"done": False})

def send_notification(alarm):
    payload = {"Authorization": "key=AAAA5czOBtU:APA91bEppY3fxfbbzc2QhnmzWpTPSM1nbXyPHTmG4hs34JDQlgdEdQRDTIgsZ_SxumikXuH4MOENBVAUTVjayafuvoAG48ca4rNPwIG--g1W_RyQGeoZp3jm7nlKQZDdOkH3KPplnvwp",
               "Content-Type": "application/json"
               }
    data = {"to": "/topics/alarms",
            "notification": {
            "title": "Alarma disparada por "+alarm.user.first_name +" "+ alarm.user.last_name,
            "body": alarm.alarm_type
          }
        }.__str__().replace('\'', '"')
    r = requests.post('https://fcm.googleapis.com/fcm/send', data=data, headers = payload)
    r.text

class PhoneAndAddress(APIView):
    def post(self, request):
        try:
            phone = request.data.get("phone")
            address = request.data.get("address")
            user_id = request.data.get("userId")
            user = User.objects.get(pk= user_id)
            user_extension = UserExtension()
            user_extension.phone = phone
            user_extension.address = address
            user_extension.user = user
            user_extension.save()
            return Response({'done':True})
        except Exception:
            return Response({'done':False})
