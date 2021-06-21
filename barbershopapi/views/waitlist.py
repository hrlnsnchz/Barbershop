"""View module for handling requests about events"""
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from barbershopapi.models import Waitlist, Barber


class WaitlistView(ViewSet):
    """Level up events"""
    
    def list(self, request):
        """Handle GET requests to events resource

        Returns:
            Response -- JSON serialized list of events
        """
        # Get the current authenticated user
        waitlists = Waitlist.objects.all()

        serializer = WaitlistSerializer(
            waitlists, many=True, context={'request': request})
        return Response(serializer.data)


class WaitlistUserSerializer(serializers.ModelSerializer):
    """JSON serializer for event organizer's related Django user"""
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class WaitlistBarberSerializer(serializers.ModelSerializer):
    """JSON serializer for event organizer"""
    user = WaitlistUserSerializer(many=False)

    class Meta:
        model = Barber
        fields = ['user']

class WaitlistSerializer(serializers.ModelSerializer):
    """JSON serializer for Waitlists"""
    barber = WaitlistBarberSerializer(many=False)

    class Meta:
        model = Waitlist
        fields = ('id', 'customer', 'barber',
                  'time', 'is_served')
        # depth = 1