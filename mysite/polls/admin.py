from django.contrib import admin

from .models import Choice, Question

# Register your models here.

# tell the admin that Question objects have an admin interface.
admin.site.register(Question)

admin.site.register(Choice)