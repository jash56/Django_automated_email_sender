from django.shortcuts import render, redirect

# Create your views here.
def form(request):
	return render(request, 'form.html')


from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

def mail(request):
	template = render_to_string('email.html')
	reciever = request.POST['rec']
	print(reciever)
	email = EmailMessage(
		'Testing mail',
		template,
		settings.EMAIL_HOST_USER,
		[reciever],
	)

	email.fail_silently = False
	email.send()

	return redirect('form')
