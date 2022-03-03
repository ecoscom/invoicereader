from pyexpat import model
from django.db import models

class Document(models.Model):
    filename = models.CharField(max_length=300)
    document = models.FileField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.filename} - {self.uploaded_at}'
