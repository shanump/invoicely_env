import email
from django.contrib.auth.models import User
from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=225)
    org_number = models.CharField(max_length=225, blank='true', null='true')
    first_invoice_number = models.IntegerField(default=1)
    bankaccount = models.CharField(max_length=225, blank='true', null='true')
    created_by = models.ForeignKey(User, related_name='teams', on_delete=models.CASCADE)
    email = models.CharField(max_length=225)
    address1 = models.CharField(max_length=225, blank='true', null='true')
    address2 = models.CharField(max_length=225, blank='true', null='true')
    zipcode = models.CharField(max_length=225, blank='true', null='true')
    place = models.CharField(max_length=225, blank='true', null='true')

    def __str__(self):
        return '%s' %self.name

