from django.db import models
from froala_editor.fields import FroalaField

LOG_STATUS = [
    ('Active', 'Active'),
    ('Pending', 'Pending'),
    ('Unresolved', 'Unresolved'),
    ('Closed', 'Closed'),
]


class CustomerLog(models.Model):
    customer_name = models.CharField(max_length=100)
    complaint_text = FroalaField(theme='dark')
    possible_solution = FroalaField(theme='dark')
    status = models.CharField(max_length=20, choices=LOG_STATUS, default='Pending', help_text="Stage act which the log is. \
        Pending is untended to Active is being tended to closed is tended to and resolved Unresolved tended to but not resolved")
    date_updated = models.DateTimeField(auto_now=True)
    date_filed = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.customer_name}'s Complaint - {self.status} - {self.date_filed}"
