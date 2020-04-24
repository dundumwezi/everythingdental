from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

def home(request):
	return render(request, 'home.html', {})


def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		subject = "Inquiry from" + ' ' + message_name
		message = message
		from_email = settings.EMAIL_HOST_USER
		recipient_list = settings.EMAIL_HOST_USER
		
		# sending email
		send_mail(subject, message, from_email, [recipient_list], fail_silently=False)

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

		subject = "Book Appointment for " + your_service
		message = "I wish to book an appointment for " + your_service + ', ' + 'scheduled for' + ' ' + your_date + ',' + ' between' + ' ' + your_schedule + '.  ' + "Regrds." + ' ' + your_name

		recipient_list = settings.EMAIL_HOST_USER
		from_email = settings.EMAIL_HOST_USER

		# sending email
		#send_mail([email_add,], your_service, your_name, your_phone, your_address, your_schedule, your_date,)
		send_mail(subject, message, from_email, [recipient_list], fail_silently=False)

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



