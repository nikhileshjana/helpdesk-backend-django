from rest_framework import serializers

from .models import TicketUser, TicketUserAddress


class TicketUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketUser
        fields = ['id', 'name', 'email', 'password', 'role']

class TicketUserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketUserAddress
        fields = ['id', 'userId', 'address']