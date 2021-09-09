from django.contrib import admin

from .models import Profile, Recipient, Mailing

# Register your models here.
admin.site.register(Profile)
admin.site.register(Recipient)
admin.site.register(Mailing)
