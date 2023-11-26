from rest_framework import serializers
from contact_us_api.models import ContactUs

class ContactUsSeralizer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'