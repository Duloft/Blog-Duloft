from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from .models import Complaint

from django.conf import settings

account_sid = settings.TWILIO_ACCOUNT_SID
auth_token = settings.TWILIO_AUTH_TOKEN

client = Client(account_sid, auth_token)

menu = """
    1. Property Listing
    2. Property Management
    3. Property Inspection
    4. Payment Options
    5. Rentals
    6. Sales
    7. Log Complaint Or Other Inquires
    8. Transfer To Customer Support Personal
    """
# every thing on rentals from payment mode ie monthly or yearly to commission, maintenance
list_of_services = {
    '1': 'Property Listing',
    '2': 'Property Management',
    '3': 'Property Inspection',
    '4': 'Payment Options',
    '5': 'Rentals', # every thing on rentals from payment mode ie monthly or yearly to commission, maintenance
    '6': 'Sales',
    '7': 'Log Complaint Or Other Inquires',
    '8': 'Transfer To Customer Support Personal'
}

greeting_message = [
    'hi', 'hey', 'hello',
    'good day', 
    'good afternoon',
    'good morning',
    'good evening'
]


def send_message(to: str, from_: str, message: str):
    client.messages.create(
                            body=message,
                            from_=from_,
                            to=to
                        )


@csrf_exempt
def handle_incoming_messages(request):
    # print(request.POST)
    # print(request.POST['Body'])
    # print(request.POST['ProfileName'])
    # print(request.POST['From'])
    if request.method == 'POST':
        incoming_message = request.POST["Body"].strip().lower()
        sender_name = request.POST["ProfileName"]
        # sender_number_details = request.POST["From"].split(':')
        sender_number = request.POST["From"]
        receiver_number = request.POST["To"]
        # print(sender_number)
        response_message = process_message(incoming_message, sender_number, sender_name)

        response = send_message(sender_number, receiver_number, response_message)
        return HttpResponse("Sent...")


# @csrf_exempt
# def handle_incoming_messages(request):
#     if request.method == 'POST':
#         incoming_message = request.POST.get('Body', '').strip().lower()
#         sender_number = request.POST.get('From', '')
#         sender_name = request.POST["ProfileName"]

#         response_message = process_message(incoming_message, sender_number, sender_name)
#         print(sender_number)
#         response = MessagingResponse()
#         response.message(response_message)
#         print(response)

#         return JsonResponse({'twiml': str(response)})
    
#     return JsonResponse({'error': 'Invalid request method'}, status=400)


def process_message(message, sender_number, sender_name):
    greeting_response = f"Hello {sender_name}, it's nice to hear from you, I am D-Bot, DuLoft chatbot assistant.\n Here is a list of what I can do for you.{menu}"
    message = message
    # print(f"in process message > {message}")
    if message in greeting_message:
        print("message in greeting")
        return greeting_response
    
    if message == "menu":
        return "Please select from the following options:\n" + "\n".join(menu)
    
    service_keys = list_of_services.keys()
    service_values = list_of_services.values()
    if message in service_keys:
        # User selected a predefined question
        return handle_predefined_question(message)
    elif message.capitalize() in service_values:
        return handle_predefined_question(message)
    else:
        # User entered a custom question
        return handle_custom_question(message, sender_number)
    


def handle_predefined_question(selected_option: str):
    if selected_option.isdigit():
        if selected_option == "1" :
            return "To list your property on our platform, you will need to provide the documents of the property. \n ie. Deed of assignment and survey plan or the CofO (Certificate of Occupancy). \n You will need a valid ID that matches the name on the documents and bank account. Before your account can be verified."
        elif selected_option == "2":
            return "Our property management services include: \n Tenant Placement and Screening \n Lease Management \n Rent Collection \n Property Maintenance and Repairs \n Financial Reporting \n Property Marketing \n Tenant Relations \n Eviction Services \n Legal Compliance \n Property Routine Inspections."
        elif selected_option == "3":
            return "You can schedule an inspection by going to our platform and select your desired property and click on the schedule inspection button. \n And our team will contact you."
        elif selected_option == "4":
            return "You can make payment through our platform or at our office"
        elif selected_option == "5":
            return "every thing on rentals from payment mode ie monthly or yearly to commission, maintenance"
        elif selected_option == "6":
            return "every thing on sales from payment mode ie monthly or yearly to commission, maintenance"
        elif selected_option == "7":
            return "Pls state your complaint... Using the keyword: My complaint....."
        elif selected_option == "8":
            return "You are being transfer to our customer support personal, this may take about ten minutes or one hour. please do hold...."
    else:
        if selected_option.lower() ==  "property listing":
            return  "To list your property on our platform, you will need to provide the documents of the property. \n ie. Deed of assignment and survey plan or the CofO (Certificate of Occupancy). \n You will need a valid ID that matches the name on the documents and bank account. Before your account can be verified."
        elif selected_option.lower() == "property management":
            return "Our property management services include: \n Tenant Placement and Screening \n Lease Management \n Rent Collection \n Property Maintenance and Repairs \n Financial Reporting \n Property Marketing \n Tenant Relations \n Eviction Services \n Legal Compliance \n Property Routine Inspections."
        elif selected_option.lower() == "property inspection":
            return "You can schedule an inspection by going to our platform and select your desired property and click on the schedule inspection button. \n And our team will contact you."
        elif selected_option.lower() == "payment options":
            return "You can make payment through our platform or at our office"
        elif selected_option.lower() == "rentals":
            return "every thing on rentals from payment mode ie monthly or yearly to commission, maintenance"
        elif selected_option.lower() == "sales":
            return "every thing on sales from payment mode ie monthly or yearly to commission, maintenance"
        elif selected_option.lower() in ("complaint", "other inquires", "inquires"):
            return "Pls state your complaint... Using the keyword: My complaint....."
        elif selected_option.lower() in ("transfer to customer support personal", "customer support", 'transfer', 'customer support personal'):
            return "You are being transfer to our customer support personal, this may take about ten minutes or one hour. please do hold...."


def handle_custom_question(message, sender_number):
    if 'my complaint' in message:
        Complaint.objects.create(sender_number=sender_number, message=message)
        return "Your complaint has been logged. Our team will get back to you shortly."
    elif 'my inquires' in message:
        Complaint.objects.create(sender_number=sender_number, message=message)
        return "Your inquires has been logged. Our team will get back to you shortly."
    else:
        return f"You entered an invalid option. please select from {menu}"


