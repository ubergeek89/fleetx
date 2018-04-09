from django.core.mail import send_mail
import requests

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

	#k = requests.post("https://api.mailgun.net/v3/mail.fleetxhq.com", auth=("api", "key-c4d137533d353762004b566344ebb11c"), data={"from": "FleetX <no-reply@fleetxhq.com>", "to": "aditya@espertosys.com", "subject": "Hello","text": "Testing some Mailgun awesomness!","html": "<html>HTML version of the body</html>"})