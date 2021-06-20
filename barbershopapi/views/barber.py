"""View module for handling requests about park areas"""
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from barbershopapi.models import Barber


class BarberView(ViewSet):
    """Barber can see profile information"""

    def list(self, request):
        """Handle GET requests to games resource
        Returns:
            Response -- JSON serialized list of games
        """
        # Get all game records from the database
        barbers = Barber.objects.all()

        # Support filtering games by type
        #    http://localhost:8000/games?type=1
        #
        # That URL will retrieve all tabletop games
        serializer = BarberSerializer(
            barbers, many=True, context={'request': request})
        return Response(serializer.data)

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
        fields = ('user',)