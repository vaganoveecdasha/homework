from django.db import models

# Create your models here.
class Form(models.Model):
    firstName = models.CharField(max_length=70, blank=False)
    lastName = models.CharField(max_length=70, blank=False)
    email = models.CharField(max_length=70, blank=False)
    text = models.CharField(max_length=1500, blank=False)
    checked = models.BooleanField(default=False, blank=False)

    def __str__(self):
        return f'{self.firstName} - {self.checked}'
