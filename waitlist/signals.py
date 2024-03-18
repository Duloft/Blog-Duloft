import smtplib
import ssl
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Waitlist
from email.message import EmailMessage as EMail
from decouple import config



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
            

        if own_a_house and not manage_my_property:
            message = "Thank You for your interest in letting us list your property. We will be contacting you soon for more updates."
            email = instance.email
            sendmailPdf(subject=subject, message=message, receiver=[email,])
            
# post_save.connect(list_saved, sender=Waitlist)


def sendmailPdf(subject: str, message: str, receiver: list):
    print("sending....")
    
    sender = 'info@duloft.com'
    password = config('ZOHO_MAIL_SECRET_KEY')
    msg = EMail()
    msg.set_content(message)
    msg['subject'] = subject
    msg['to'] = receiver
    msg['from'] = sender
    
    context = ssl.create_default_context()
    # Connect to the SMTP server using TLS
    server = smtplib.SMTP("smtppro.zoho.com", 587)
    print('starting TLS...')
    server.starttls(context=context)  # Start TLS encryption
    server.login(sender, password)
    server.send_message(msg)
    
    server.quit()
    
    # sender = 'info@duloft.com'
    # email = EmailMessage(
    #     subject,
    #     message,
    #     sender,
    #     receiver,
    # )
    # # Send the email
    # email.send(fail_silently=False)
    print('mail sent')