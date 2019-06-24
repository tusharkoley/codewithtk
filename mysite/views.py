from django.shortcuts import render,  get_object_or_404
from .forms import ContactForm, NotificationForm
from django.core.mail import send_mail,send_mass_mail
from django.contrib.auth.models import User


def contact_us( request):
	form = ContactForm()
	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			
			fName=form.cleaned_data['firstName']
			lName=form.cleaned_data['lastName'] 
			from_email=form.cleaned_data['email'] 
			to_email=['info.dgtit@gmail.com','tusharkoley@gmail.com']
			subject=form.cleaned_data['subject'] 
			message=form.cleaned_data['message']

			message=" Sender Name : {} {} . \n Sender Email Id {}. \n The message is : {} ". format(fName, lName,from_email, message)


			send_mail(subject,message,'runakoley3@gmail.com',to_email,fail_silently=False,)
			return render (request, "contact_confirm.html",{})
            
		else:
			form = ContactForm()
    
	return render (request, "contact_us.html",{'form': form})


def send_notification_all( request):
	form = NotificationForm()
	if request.method == "POST":
		form = NotificationForm(request.POST)
		if form.is_valid():				
			from_email='admin@dgtit.com'
			users=User.objects.all()
			to_email=[user.email for user in users]
			sender_email='info.dgtit@gmail.com'

			subject=form.cleaned_data['subject'] 
			message=form.cleaned_data['message']

			
			send_mail(subject,message,sender_email,to_email,fail_silently=True,)
			return render (request, "notification_confirm.html",{})
            
		else:
			form = NotificationForm()
    
	return render (request, "send_notification.html",{'form': form})





def home(request):
	return render(request,"home.html", {}) 

def team( request):
	return render (request, "team.html",{})

def index( request):
    return render (request, "apps_index.html",{})
