from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from barbershopapi.models import Customer
from django.contrib.auth.models import User


class CustomerView(ViewSet):

    def list(self, request):
        """Handle GET requests to customers resource
        Returns:
            Response -- JSON serialized customer item
        """
        customer = Customer.objects.get(user=request.auth.user)

        serializer = CustomerSerializer(
            customer, many=False, context={'request': request})
        return Response(serializer.data)

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for gamer's related Django user"""
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for customers"""
    user = UserSerializer(many=False)
    class Meta:
        model = Customer
        fields = ('user',)
        depth = 1