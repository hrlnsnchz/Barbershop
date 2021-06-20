"""View module for handling requests about park areas"""
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from barbershopapi.models import Service


class ServiceView(ViewSet):
    """Service can see profile information"""

    def list(self, request):
        """Handle GET requests to games resource
        Returns:
            Response -- JSON serialized list of games
        """
        # Get all game records from the database
        services = Service.objects.all()

        # Support filtering games by type
        #    http://localhost:8000/games?type=1
        #
        # That URL will retrieve all tabletop games
        serializer = ServiceSerializer(
            services, many=True, context={'request': request})
        return Response(serializer.data)



class ServiceSerializer(serializers.ModelSerializer):
    """JSON serializer for services"""

    class Meta:
        model = Service
        fields = ('label', 'price')

