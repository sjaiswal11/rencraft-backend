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
