from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.views import APIView
from .serializers import *
from rest_framework import viewsets, status


# Create your views here.


class EnquiryApi(APIView):
    def get(self, request):
        Enquiry = enquiryDatas.objects.all()
        # print(Enquiry)
        serializer_datas = EnquirySerializers(Enquiry, many=True)

        return Response(serializer_datas.data)

    def post(self, request):
        serializer = EnquirySerializers(data=request.data)
        print(serializer.is_valid())
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class productApi(APIView):
    def get(self, request):
        product_ = product.objects.all()
        print(product_)
        serializer_datas = productSerializers(product_, many=True)

        return Response(serializer_datas.data)

    def post(self, request):

        serializer = productSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)