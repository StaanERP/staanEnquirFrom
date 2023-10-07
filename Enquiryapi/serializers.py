from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token


class productSerializers(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = "__all__"


class EnquirySerializers(serializers.ModelSerializer):
    class Meta:
        model = enquiryDatas
        fields = "__all__"
