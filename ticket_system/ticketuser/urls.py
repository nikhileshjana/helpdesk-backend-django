from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TicketUserViewSet, TicketUserAddressViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'ticketuser', TicketUserViewSet, basename='ticketuser')
router.register(r'ticketuseraddress', TicketUserAddressViewSet, basename='ticketuseraddress')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]