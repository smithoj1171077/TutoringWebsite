from django.contrib import admin
from .models import Blog
from studentrequest.models import Subject
# Register your models here.

# enable the admin to view the DB entries for Blog and Subject
admin.site.register(Blog)
admin.site.register(Subject)
