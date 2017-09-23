from django.db import models
from django.utils import timezone
from django.http import JsonResponse

# Create your models here.


class Company(models.Model):
    """This class represents the bucketlist model."""
    name = models.CharField(max_length=50, blank=False, unique=True)
    initials = models.CharField(max_length=4, blank=False, unique=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)


class Dock(models.Model):
    """This class represents the bucketlist model."""
    initials = models.ForeignKey('Company')
    value = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    @property
    def company(self):
        return Company.objects.filter(pk=self.initials.pk).values().first()

    @company.setter
    def company(self, value):
        self.initials = value

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.initials)


