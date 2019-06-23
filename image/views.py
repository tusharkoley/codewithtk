from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ImageUpdateForm
from .models import Edge
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView

)


@login_required
def edge(request):

	form = ImageUpdateForm(request.POST)

	if  form.is_valid():
		form.save()
		messages.success(request, f'Image Succesfully Updated!')
		return redirect('home')

	context= {'form': form }

	return render(request, 'image/find_edge.html', { context})


class ImageCreateView(LoginRequiredMixin,CreateView):
    model = Edge
    fields = ['image']
    template_name = 'image/find_edge.html' 
    success_url = '/image/list'

    def form_valid(self, form):
        form.instance.user = self.request.user

   

        if form.instance.image.url.find('default.jpg') >=0 :
            messages.error(self.request, f'Please select an Image!')
            return super().form_invalid(form)
        return super().form_valid(form)
 
    
def results(request):
    img=Edge.objects.filter(user=request.user).order_by('-date_posted')[0]

    print('**********')
    print(request.user)

    return render(request, 'image/detail.html', {'img': img})


class ImgtDeleteView(LoginRequiredMixin, DeleteView):
    model = Edge
    success_url = '/image'
    template_name = 'image/find_edge.html'

    def test_func(self):
      
        return True
