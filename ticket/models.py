import uuid
from django.db import models
from users.models import User
#from django.contrib.auth.models import User

class Ticket(models.Model):
    status_choices=(
        ('Active','Active'),
        ('completed','completed'),
        ('pending','pending')

    )
    ticket_number=models.UUIDField(default=uuid.uuid4)
    title=models.CharField(max_length=100)
    description=models.TextField()
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='created_by')
    date_created=models.DateTimeField(auto_now_add=True)

    assigned_to = models.ForeignKey(User, related_name='assigned_tickets', null=True, blank=True, on_delete=models.SET_NULL)

    is_resolved=models.BooleanField(default=False)
    accepted_date=models.DateTimeField(null=True,blank=True)
    closed_date=models.DateTimeField(null=True,blank=True)
    ticket_status=models.CharField(max_length=15,choices=status_choices)
    solution = models.TextField(null=True, blank=True)
    customer_report = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.title
   
class Technician(models.Model):
    username = models.CharField(max_length=100, unique=True)
    # other fields...

    def __str__(self):
        return self.username



class Notification(models.Model):
    technician = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

class BuyRequest(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    item_title = models.CharField(max_length=255)
    item_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class ReportRequest(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    item_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
