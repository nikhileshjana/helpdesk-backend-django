from rest_framework import viewsets, pagination
from rest_framework.response import Response
from .models import Ticket, Comment, StatusType, IssueLocationType, IssueType
from .serializers import TicketSerializer, CommentSerializer, StatusTypeSerializer, IssueLocationTypeSerializer, \
    IssueTypeSerializer


class StatusTypeViewSet(viewsets.ModelViewSet):
    queryset = StatusType.objects.all().order_by('desc')
    serializer_class = StatusTypeSerializer

class IssueTypeViewSet(viewsets.ModelViewSet):
    queryset = IssueType.objects.all().order_by('desc')
    serializer_class = IssueTypeSerializer

class IssueLocationTypeViewSet(viewsets.ModelViewSet):
    queryset = IssueLocationType.objects.all().order_by('desc')
    serializer_class = IssueLocationTypeSerializer

class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size_query_param = 'limit' # Allows frontend to change items per page
    max_page_size = 100

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all().order_by('-created_at')
    serializer_class = TicketSerializer
    pagination_class = StandardResultsSetPagination

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer