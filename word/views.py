from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from word import pdataread

def resume(request):
	print('*********inside Resume*****')

	path = '/Users/tusharkoley/code2/djangoproject/word/tushar.docx'

	dictResults=pdataread.procResume(path)
	print('********Dictionary *****')
	print(dictResults)
	return render(request, 'word/resume.html', {'dictResults':dictResults})


	

    
    
    
