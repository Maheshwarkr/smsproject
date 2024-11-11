from django.contrib import admin

from django.contrib import admin
from .models import *
from .models import Contact

admin.site.register(Task)

from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'feedback')





admin.site.register(Contact)