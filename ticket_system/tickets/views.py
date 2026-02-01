from rest_framework import viewsets, pagination
from rest_framework.response import Response
from .models import Ticket
from .serializers import TicketSerializer

class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size_query_param = 'limit' # Allows frontend to change items per page
    max_page_size = 100

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all().order_by('-created_at')
    serializer_class = TicketSerializer
    pagination_class = StandardResultsSetPagination

    # Example: Custom endpoint to add a comment
    def perform_create(self, serializer):
        serializer.save(recorded_by=self.request.user)