from django.db import models


class Blog(models.Model):
    summary_header = models.CharField(max_length=100)
    description = models.TextField(max_length=20000)
    date = models.DateField()
    #image = models.ImageField(upload_to="blog/images/")

    def __str__(self):
        return self.summary_header