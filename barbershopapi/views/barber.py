"""View module for handling requests about park areas"""
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from barbershopapi.models import Appointment, Barber, Service


class Profile(ViewSet):
    """Barber can see profile information"""

    def list(self, request):
        """Handle GET requests to profile resource
        Returns:
            Response -- JSON representation of user info and Appointments
        """
        barber = Barber.objects.get(user=request.auth.user)
        appointments = Appointment.objects.filter(attendees=barber)

        appointments = AppointmentSerializer(
            appointments, many=True, context={'request': request})
        barber = BarberSerializer(
            barber, many=False, context={'request': request})

        # Manually construct the JSON structure you want in the response
        profile = {}
        profile["barber"] = barber.data
        profile["appointments"] = appointments.data

        return Response(profile)

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for barber's related Django user"""
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')


class BarberSerializer(serializers.ModelSerializer):
    """JSON serializer for barbers"""
    user = UserSerializer(many=False)

    class Meta:
        model = Barber
        fields = ('user')


class ServiceSerializer(serializers.ModelSerializer):
    """JSON serializer for services"""
    class Meta:
        model = Service
        fields = ('label', 'price')


class AppointmentSerializer(serializers.ModelSerializer):
    """JSON serializer for appointments"""
    service = ServiceSerializer(many=False)

    class Meta:
        model = Appointment
        fields = ('id', 'customer', 'barber', 'datetime', 'services')