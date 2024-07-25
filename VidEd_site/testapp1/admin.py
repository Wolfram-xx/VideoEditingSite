from django.contrib import admin
from testapp1.models import *
# Register your models here.

# admin.site.register(User)
# admin.site.register(Message)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'date', 'address')
