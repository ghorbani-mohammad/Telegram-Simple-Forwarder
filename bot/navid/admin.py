from django.contrib import admin

from .models import Channel, Bot

@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'username')
    search_fields = ['name', 'username']


@admin.register(Bot)
class BotAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'token')
    search_fields = ['name']