from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']


class productSerializers(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = "__all__"


class ConferenceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Conferencedata
        fields = "__all__"


class EnquirySerializers(serializers.ModelSerializer):
    # Use the ConferencedataSerializer for the nested field

    class Meta:
        model = enquiryDatas
        fields = "__all__"
