from django.core.mail import send_mail

def send_email(subject, to, html_message):
	from_email = 'FleetX <no-reply@fleetxhq.com>'
	send_mail(
	    subject = subject,
	    message = html_message,
	    html_message = html_message,
	    from_email = from_email,
	    recipient_list = [to],
	    fail_silently=False,
	)