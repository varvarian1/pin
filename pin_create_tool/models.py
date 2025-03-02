from django.db import models

class Pin(models.Model):
    title = models.CharField('Title', max_length=50)
    pin = models.ImageField('Pin', upload_to='pins/')
    description = models.CharField('Description', max_length=150)

    def __str__(self):
        return self.title
