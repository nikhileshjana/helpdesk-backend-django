from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import TicketUser, TicketUserAddress
from .serializers import TicketUserSerializer, TicketUserAddressSerializer


# Create your views here.
class TicketUserViewSet(viewsets.ModelViewSet):
    queryset = TicketUser.objects.all().order_by('name')
    serializer_class = TicketUserSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['role']
    search_fields = ['name', 'email']

class TicketUserAddressViewSet(viewsets.ModelViewSet):
    queryset = TicketUserAddress.objects.all().order_by('-created_at')
    serializer_class = TicketUserAddressSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['userId']