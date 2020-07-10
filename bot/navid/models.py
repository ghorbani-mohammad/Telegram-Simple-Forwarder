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


class Bot(BaseModel):
    name = models.CharField(blank=True, max_length=100, null=True)
    token = models.CharField(max_length=100)

    def __str__(self):
        return self.name

