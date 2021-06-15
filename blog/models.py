from django.db import models
from tinymce import models as tinymce_models

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    category = models.CharField(max_length=200)
    slug = models.CharField(max_length=100)
    keyword = models.CharField(max_length=200)
    content = tinymce_models.HTMLField(max_length=5000)
    timestamp = models.DateTimeField(blank=True)


    def __str__(self):
        return self.title