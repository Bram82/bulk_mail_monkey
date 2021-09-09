from django.conf import settings
from django.db import models

from customUser.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.RESTRICT, related_name='profile')

    def __str__(self):
        if self.user.first_name:
            return f'{self.user.first_name} {self.user.last_name}'
        else:
            return self.user.email


class Recipient(models.Model):
    name = models.CharField(max_length=264, blank=True)
    email = models.EmailField(blank=False, null=False)

    def __str__(self):
        return self.email


class Mailing(models.Model):
    sender = models.ForeignKey(to=Profile, on_delete=models.CASCADE, related_name='mailings')
    recipients = models.ManyToManyField(to=Recipient, related_name='mailings')

    title = models.CharField(max_length=264, blank=False)
    subject = models.CharField(max_length=264, blank=False)
    text = models.TextField(blank=False)

    @property
    def number_recipients(self):
        return self.recipients.all().count()

    def __str__(self):
        return self.title
