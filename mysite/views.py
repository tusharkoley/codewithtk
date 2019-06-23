from django.shortcuts import render,  get_object_or_404


def contact_us( request):
	return render (request, "contact_us.html",{})

def home(request):
	return render(request,"home.html", {}) 

def team( request):
	return render (request, "team.html",{})

def index( request):
    return render (request, "apps_index.html",{})
