from django.db import models
from django.core.exceptions import ValidationError


class Ticket(models.Model):
    description = models.TextField()
    status = models.CharField(max_length=20, default='open')
    issue_type = models.CharField(max_length=50)
    location_type = models.CharField(max_length=50)
    issue_location = models.CharField(max_length=255)

    # Stakeholders
    end_user = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    recorded_by = models.CharField(max_length=255, blank=True)

    # Assignments
    assigned_vendor = models.CharField(max_length=255, blank=True)
    assigned_engineers = models.CharField(max_length=255, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    closed_at = models.DateTimeField(null=True, blank=True)

    def clean(self):
        # Enforce the "Max 2 Engineers" rule at the database level
        if self.pk and self.assigned_engineers.count() > 2:
            raise ValidationError("A ticket cannot have more than 2 assigned engineers.")


class Comment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='comment_history')
    author_id = models.CharField(max_length=255, blank=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']  # Ensures chronological conversation flow