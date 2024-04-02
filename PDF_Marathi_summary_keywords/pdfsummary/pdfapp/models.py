from django.db import models

# Create your models here.
from django.db import models

class UploadedPDF(models.Model):
    document = models.FileField(upload_to='pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
