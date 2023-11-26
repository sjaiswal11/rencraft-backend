from django.shortcuts import render
from rest_framework.views import APIView
from contact_us_api.models import ContactUs
from contact_us_api.serializers import ContactUsSeralizer
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
# Create your views here.

class ContactUsListView(APIView):
    def get(self,request):
        person = ContactUs.objects.all()
        serializer = ContactUsSeralizer(person, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ContactUsSeralizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            contact_data=serializer.data
            subject = "Web_Inquiry for product"
            sender = 'fightersunny111@gmail.com'
            body = f"Name: {contact_data['name']}\nEmail: {contact_data['email']}\nMessage: {contact_data['message']}"
            reciever = 'contact_us@rencraft.in'                
            
            send_mail(subject,body, sender, [reciever])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProductContactUsView(APIView):
    def post(self,request):
        try:
            contact_data=request.data
            print(contact_data)
            subject = "Web Product page inquiry"
            sender = 'fightersunny111@gmail.com'
            body = f"Phone: {contact_data['phone']}\nEmail: {contact_data['email']}\nMessage: {contact_data['message']}"
            reciever = 'contact_us@rencraft.in'                
            send_mail(subject,body, sender, [reciever])
            return Response(status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetQuotetionView(APIView):
    def post(self,request):
        try:
            contact_data=request.data
            print(contact_data)
            subject = "Price page Inquiry"
            sender = 'fightersunny111@gmail.com'
            body = f"Category: {contact_data['category']}\nQuantity: {contact_data['quantity']}\nName: {contact_data['name']}\nEmail: {contact_data['email']}\nMessage: {contact_data['message']}"
            reciever = 'contact_us@rencraft.in'                
            send_mail(subject,body, sender, [reciever])
            return Response(status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
