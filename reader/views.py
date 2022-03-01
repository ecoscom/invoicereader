from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import UploadFileForm
from django.conf import settings
from .pdfreader import nota_BTG
from .models import Document

# Create your views here

def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            myfile = request.FILES['document']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            document = Document(filename=filename, document=myfile)
            document.save()

            uploaded_file_url = fs.url(filename)
            html_code = nota_BTG(settings.MEDIA_ROOT + '/' + filename)
            
            return HttpResponse(html_code.to_html())
    else:
        form = UploadFileForm()

    return render(request, 'reader/index.html', {'form': form})