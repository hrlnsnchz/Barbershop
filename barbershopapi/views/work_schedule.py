"""View module for handling requests about events"""
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from barbershopapi.models import Work_Schedule, Barber


class Work_ScheduleView(ViewSet):
    """Level up events"""
    
    def list(self, request):
        """Handle GET requests to events resource

        Returns:
            Response -- JSON serialized list of events
        """
        # Get the current authenticated user
        work_schedules = Work_Schedule.objects.all()

        serializer = Work_ScheduleSerializer(
            work_schedules, many=True, context={'request': request})
        return Response(serializer.data)


class Work_ScheduleUserSerializer(serializers.ModelSerializer):
    """JSON serializer for event organizer's related Django user"""
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class Work_ScheduleBarberSerializer(serializers.ModelSerializer):
    """JSON serializer for event organizer"""
    user = Work_ScheduleUserSerializer(many=False)

    class Meta:
        model = Barber
        fields = ['user']

class Work_ScheduleSerializer(serializers.ModelSerializer):
    """JSON serializer for Work_Schedules"""
    barber = Work_ScheduleBarberSerializer(many=False)

    class Meta:
        model = Work_Schedule
        fields = ('id', 'barber',
                  'working_from', 'working_to')
        # depth = 1