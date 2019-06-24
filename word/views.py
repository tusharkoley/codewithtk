from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import UploadDocForm


from .pdataread import procResume, handle_uploaded_file



def upload_doc(request):
	form = UploadDocForm()
	if request.method == 'POST':
		form = UploadDocForm(request.POST, request.FILES)
		print('*******Request POST ****')
		if form.is_valid():
			f=request.FILES['file']
			if '.docx' in str(f):
				#handle_uploaded_file(f)  
				print('****After Handle File')    
				dictResults=procResume(f)
				return render(request, 'word/resume.html', {'dictResults':dictResults})
			else:
				print('****Incorrect File format***')
				messages.warning(request, '**Incorrect File format**.')
				

			
		else:
			print('****The form is invalid***')
			
			
	else:
		
		print('****FRequest is not Post')
	return render(request, 'word/resume_upload.html', {'form': form})
			