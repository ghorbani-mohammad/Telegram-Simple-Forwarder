from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Channel(BaseModel):
    name = models.CharField(blank=True, max_length=100, null=True)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Broker(BaseModel):
    name = models.CharField(blank=True, max_length=100, null=True)
    source_channels = models.ManyToManyField(
        Channel, related_name="source_bots", related_query_name="source_bot"
    )
    destination_channels = models.ManyToManyField(
        Channel, related_name="destination_bots", related_query_name="destination_bot"
    )

    def __str__(self):
        return self.name
