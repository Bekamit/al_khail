from django.db import models
from solo.models import SingletonModel


class Company(SingletonModel):
    company_name = models.CharField(max_length=50)
    about = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    company_img = models.ImageField(upload_to='company/')
    # contact_person = models.CharField(max_length=10)

    def __str__(self):
        return self.company_name
