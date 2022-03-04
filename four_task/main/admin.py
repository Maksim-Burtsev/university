from django.contrib import admin

from main.models import Phone

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    pass