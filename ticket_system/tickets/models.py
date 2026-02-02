from django.db import models
from django.core.exceptions import ValidationError


class StatusType(models.Model):
    cd = models.CharField(max_length=20, primary_key=True)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.desc

class IssueType(models.Model):
    cd = models.CharField(max_length=20, primary_key=True)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.desc

class IssueLocationType(models.Model):
    cd = models.CharField(max_length=20, primary_key=True)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.desc

class Ticket(models.Model):
    description = models.TextField()
    status = models.ForeignKey(StatusType, on_delete=models.CASCADE)
    issue_type = models.ForeignKey(IssueType, on_delete=models.CASCADE)
    location_type = models.ForeignKey(IssueLocationType, on_delete=models.CASCADE)
    issue_location = models.CharField(max_length=255)

    # Stakeholders
    end_user = models.CharField(max_length=255, blank=True)
    recorded_by = models.CharField(max_length=255, blank=True)

    # Assignments
    assigned_vendor = models.CharField(max_length=255, blank=True)
    assigned_engineers = models.JSONField(default=list, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    closed_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def clean(self):
        # For JSONField, assigned_engineers is a standard Python list
        if isinstance(self.assigned_engineers, list) and len(self.assigned_engineers) > 2:
            raise ValidationError("A ticket cannot have more than 2 assigned engineers.")


class Comment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='comment_history')
    author_id = models.CharField(max_length=255, blank=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']  # Ensures chronological conversation flow