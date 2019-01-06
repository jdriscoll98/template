from django.contrib import admin
from website.models import Employee, ScheduledShift, PostShift

admin.site.register(Employee)
admin.site.register(ScheduledShift)
admin.site.register(PostShift)
