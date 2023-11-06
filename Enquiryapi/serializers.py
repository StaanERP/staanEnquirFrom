from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ('email', 'user_name', 'password')
        extra_kwargs = {'password': {'write_olny': True}}

    def create(self, validated_data):

        password = validated_data.pop('password', None)
        print(password)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    #
    # {
    # "email":'jega@gmail.com',
    #  "user_name":"nnnn",
    #  "password": 'jega123'
    #  }


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
