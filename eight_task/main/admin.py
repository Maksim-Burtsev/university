from django.contrib import admin

from main.models import Player, Team

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    pass

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass