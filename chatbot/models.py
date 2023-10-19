from django.db import models

class Complaint(models.Model):
    sender_number = models.CharField(max_length=50)
    message = models.TextField()
    done = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
