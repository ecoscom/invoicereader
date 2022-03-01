from pyexpat import model
from django.db import models

class Document(models.Model):
    filename = models.CharField()
    document = models.FileField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
