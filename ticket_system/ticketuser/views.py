from django.shortcuts import render
from rest_framework import viewsets

from .models import TicketUser, TicketUserAddress
from .serializers import TicketUserSerializer, TicketUserAddressSerializer


# Create your views here.
class TicketUserViewSet(viewsets.ModelViewSet):
    queryset = TicketUser.objects.all().order_by('-created_at')
    serializer_class = TicketUserSerializer

class TicketUserAddressViewSet(viewsets.ModelViewSet):
    queryset = TicketUserAddress.objects.all().order_by('-created_at')
    serializer_class = TicketUserAddressSerializer