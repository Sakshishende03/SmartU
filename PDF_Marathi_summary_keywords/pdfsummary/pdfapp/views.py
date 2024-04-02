from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import UploadPDFForm
from .pdf_processor import process_pdf

def upload_pdf(request):
    if request.method == 'POST':
        form = UploadPDFForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_pdf = form.save()
            summary, keywords = process_pdf(uploaded_pdf.document)
            return render(request, 'testapp/summary.html', {'summary': summary, 'keywords': keywords})
    else:
        form = UploadPDFForm()
    return render(request, 'testapp/upload_pdf.html', {'form': form})




