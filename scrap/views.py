from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .models import Index

from scrap import search




class IndexView(generic.ListView):
    template_name = 'scrap/index.html'
    context_object_name = 'latest_search_list'

    def get_queryset(self):
        """Return the last five published Search."""
        return Index.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Index
    
    template_name = 'scrap/detail.html'
    
    

def results(request, index_id):
    index = get_object_or_404(Index, pk=index_id)

    l1 = len(index.results_set.all())

    if(l1==0):
        s1=search.doSearch(index) 
    
    return render(request, 'scrap/detail.html', {'index': index})



    


class IndexCreateView(LoginRequiredMixin,generic.CreateView):
    model = Index
    success_url = '/scrap/'
    fields = ['site_url', 'search_text']
    

    def form_valid(self, form):
        form.instance.author = self.request.user
        
        return super().form_valid(form)



   







