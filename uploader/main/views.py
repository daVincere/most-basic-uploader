from django.shortcuts import render, redirect

# For getting the settings I guess
from django.conf import settings
# 
from .forms import UploadForm
#
from django.core.files.storage import FileSystemStorage
#

def upload_direct(request): 
	if request.method == 'POST' and request.FILES['file']:
		file = request.FILES['file']
		fs = FileSystemStorage()
		filename = fs.save(file.name, file)
		uploaded_file_url = fs.url(filename)

		context = {
			'uploaded_file_url' : uploaded_file_url,
		}
		return render(request, "main_upload.html", context)

	return render(request, "main_upload.html")

# Create your views here.
def index(request):
	return render(request, "home.html", {})



def upload_model_form(request):
	if request.method =='POST':
		form = UploadForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')
	
	else:
		form = UploadForm()

	context = {
		'form':form,
	}
		
	return render(request, 'model_form_upload.html',context)
	
