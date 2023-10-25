from django.db import models

# Create your models here.
class File(models.Model):
  title = models.CharField(max_length=256)
  description = models.TextField()
  attachement = models.FileField(upload_to='uploaded_files/')
