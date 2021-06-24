"""View module for handling requests about events"""
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from barbershopapi.models import Appointment, Barber, Customer


class AppointmentView(ViewSet):
    """Barbershop appointments"""

    def create(self, request):
        """Handle POST operations for waitlists
        Returns:
            Response -- JSON serialized waitlist instance
        """
        appointment = Appointment()
        customer = Customer.objects.get(user=request.auth.user)
        appointment.barber = Barber.objects.get(pk=request.data['barber'])
        appointment.start = request.data["start"]
        appointment.end = request.data['end']
        appointment.customer = customer
        

        try:
            appointment.save()
            appointment.appointment_services.set(request.data["appointment_services"])
            serializer = AppointmentSerializer(appointment, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        """Handle GET requests to events resource

        Returns:
            Response -- JSON serialized list of events
        """
        # Get the current authenticated user
        # barber = Barber.objects.get(user=request.auth.user)
        appointments = Appointment.objects.all()

        # Set the `joined` property on every event

        serializer = AppointmentCalendarSerializer(
            appointments, many=True, context={'request': request})
        return Response(serializer.data)


class AppointmentUserSerializer(serializers.ModelSerializer):
    """JSON serializer for event organizer's related Django user"""
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class AppointmentBarberSerializer(serializers.ModelSerializer):
    """JSON serializer for event organizer"""
    user = AppointmentUserSerializer(many=False)

    class Meta:
        model = Barber
        fields = ['user']

class AppointmentCalendarSerializer(serializers.ModelSerializer):
    """JSON serializer for appointments"""
    # barber = AppointmentBarberSerializer(many=False)

    class Meta:
        model = Appointment
        fields = ('id',
                  'start', 'end')

class AppointmentSerializer(serializers.ModelSerializer):
    """JSON serializer for appointments"""
    barber = AppointmentBarberSerializer(many=False)

    class Meta:
        model = Appointment
        fields = ('id', 'barber', 'customer',
                  'start', 'end', 'appointment_services')
