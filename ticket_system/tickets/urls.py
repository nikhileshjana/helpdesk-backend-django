from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TicketViewSet, StatusTypeViewSet, IssueTypeViewSet, IssueLocationTypeViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'statustype', StatusTypeViewSet, basename='statustype')

# ADD THESE TWO LINES:
router.register(r'issuetype', IssueTypeViewSet, basename='issuetype')
router.register(r'locationtype', IssueLocationTypeViewSet, basename='locationtype')

# Uncomment this if you want to access tickets at /api/tickets/
router.register(r'', TicketViewSet, basename='ticket')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]