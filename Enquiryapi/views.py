import os

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.views import APIView
from .serializers import *
from rest_framework import viewsets, status
from django.core.mail import EmailMessage
from pathlib import Path


# Create your views here.


def send_email(request, to, pdf_file_paths):
    subject = 'Testing Email'
    body = """Dear Sir/Madam,
It’s very nice meeting you at conference.

We, STAAN Biomed Engineering Private Limited was established in the year of 2003, as a leading manufacturer of Surgical Operating Tables, Surgical Operating Lights, Anesthesia Workstation, ICU Ventilators, HFNC (High Flow Nasal Cannula), Tourniquet, Surgical Instruments, Critical Care Devices. Our Organisation is an ISO 9001:2015 (Quality Management Systems & Requirements) & EN ISO 13485:2016 (Medical Devices – Quality Management Systems – Requirements) Certified Company.

Also, we do have recognition from world’s leading certification bodies like TUV SUD, ITC, ICR Polaska Co Ltd. And our Class I – Medical Devices are CE marked and US FDA registered. We are doing PAN India supply as a competitive manufacturer and exporter of Medical Devices.

We have successfully completed more than 550 Hospital projects directly and as well as through our dealer network, particularly in Orthopaedics, Gynaecology & Obsterics, Neuro, Vascular, Laparoscopy, Gastroenterology, Spine and General Surgery Operation Theatres and Intensive Care Units.

Please feel free to contact us for your requirements.

STAAN Biomed Engineering Private Limited

+91-98422 19018 | sales@staan.in | www.staan.in
T: +91-422 2533806 | +91-422 2531008 | +91-422 2537440"""
    To = [to]

    # Create an EmailMessage object
    email = EmailMessage(subject, body, 'jegathish.e@staan.in', To)

    BASE_DIR = Path(__file__).resolve().parent.parent
    pdf_path = BASE_DIR / "PDF"

    # Attach multiple PDF files to the email
    for pdf_file_path in pdf_file_paths:
        try:
            # Normalize the path using os.path.join to handle backslashes
            normalized_path = os.path.join(pdf_path, pdf_file_path)

            with open(normalized_path, 'rb') as file:
                file_name = os.path.basename(pdf_file_path)  # Extract file name using os.path.basename
                print(normalized_path, "with base name")
                email.attach(file_name, file.read(), 'application/pdf')
        except Exception as e:
            print(f"Error attaching file {pdf_file_path}: {e}")

    # Send the email
    try:
        email.send()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")


class EnquiryApi(APIView):

    def get(self, request):
        Enquiry = enquiryDatas.objects.all()

        serializer_datas = EnquirySerializers(Enquiry, many=True)

        return Response(serializer_datas.data)

    def post(self, request):
        serializer = EnquirySerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            email_value = serializer.validated_data.get('Email')
            intrested = serializer.validated_data.get('Interesteds')
            BASE_DIR = Path(__file__).resolve().parent.parent
            pdf_path = BASE_DIR / "PDF"
            intrested_list = []
            for data in intrested:
                # print(pdf_path / str(data))
                data = str(data)+".pdf"
                intrested_list.append(pdf_path / str(data))

            send_email(request, email_value, intrested_list)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EnquiryDetails(APIView):
    def get_object(self, pk):
        try:
            return enquiryDatas.objects.get(pk=pk)
        except Exception as e:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        article = self.get_object(pk)
        serialzer = EnquirySerializers(article)
        return Response(serialzer.data)

    def put(self, request, pk):
        print(request)
        article = self.get_object(pk)
        serializer = EnquirySerializers(article, data=request.data)
        print(serializer.is_valid())
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
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


class productDetails(APIView):
    def get_object(self, pk):
        try:
            return product.objects.get(pk=pk)
        except Exception as e:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        article = self.get_object(pk)
        serialzer = productSerializers(article)
        return Response(serialzer.data)


class conferenceApi(APIView):
    def get(self, request):
        Conference_ = Conferencedata.objects.all()
        # print(Conference_)
        serializer_datas = ConferenceSerializers(Conference_, many=True)

        return Response(serializer_datas.data)

    def post(self, request):
        serializer = ConferenceSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class conferenceDetails(APIView):
    def get_object(self, pk):
        try:
            return Conferencedata.objects.get(pk=pk)
        except Exception as e:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        article = self.get_object(pk)
        serialzer = ConferenceSerializers(article)
        return Response(serialzer.data)

    #
    def put(self, request, pk):
        print(request)
        article = self.get_object(pk)
        serializer = ConferenceSerializers(article, data=request.data)
        print(serializer.is_valid())
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #
    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
