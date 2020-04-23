from django.shortcuts import render
from dentist.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

def home(request):
	return render(request, 'home.html', {})


def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']
		
		subject = 'Inquiry'

		# sending email
		send_mail(
			subject,
			message_name, # sender's name
			message, # message
			message_email, # sender's email address
			[EMAIL_HOST_USER], # receiver
			)

		return render(request, 'contact.html', {'message_name': message_name})
	else:
		return render(request, 'contact.html', {})

def about(request):
	return render(request, 'about.html', {})

def service(request):
	return render(request, 'service.html', {})

def pricing(request):
	return render(request, 'pricing.html', {})

def appointment(request):
	if request.method == "POST":
		your_name = request.POST['your-name']
		your_phone = request.POST['your-phone']
		your_email = request.POST['your-email']
		your_address = request.POST['your-address']
		your_schedule = request.POST['your-schedule']
		your_date = request.POST['your-date']
		your_service = request.POST['your-service']

		# sending email
		send_mail(
			your_service, # sender's needed service as email subject
			your_name, # message
			your_phone, # sender's email address
			your_address,
			your_schedule,
			your_date,
			[EMAIL_HOST_USER], # receiver
			)

		return render(request, 'appointment.html', {
			'your_name': your_name,
			'your_phone': your_phone,
			'your_email': your_email,
			'your_address': your_address,
			'your_schedule': your_schedule,
			'your_date': your_date,
			'your_service': your_service,
			})
	else:
		return render(request, 'home.html', {})
	

