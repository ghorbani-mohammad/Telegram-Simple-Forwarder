from django.contrib import admin

from .models import Channel, Broker


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "username",
    )
    search_fields = ("name", "username")


@admin.register(Broker)
class BrokerAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
