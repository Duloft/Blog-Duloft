from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Waitlist
from django.core.mail import EmailMessage




@receiver(post_save, sender=Waitlist)
def list_saved(sender, instance, created, **kwargs):
    if created:
        subject = "DuLoft Confirmation Message"
        own_a_house = instance.own_a_house
        manage_my_property = instance.manage_my_property
        
        if own_a_house and manage_my_property:
            message = "Thank You for your interest in letting us list and manage your property. We will be contacting you soon for more updates."
            email = instance.email
            sendmailPdf(subject=subject, message=message, receiver=[email,])
            

        if own_a_house:
            message = "Thank You for your interest in letting us list your property. We will be contacting you soon for more updates."
            email = instance.email
            sendmailPdf(subject=subject, message=message, receiver=[email,])
            
# post_save.connect(list_saved, sender=Waitlist)


def sendmailPdf(subject: str, message: str, receiver: list):
    sender = 'info@duloft.com'
    email = EmailMessage(
        subject,
        message,
        sender,
        receiver,
    )
    # Send the email
    email.send()
    print('mail sent')