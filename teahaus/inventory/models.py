from django.db import models

from teahaus.users.models import User


class TeaType(models.Model):
    name = models.CharField(max_length=256)
    temperature = models.FloatField()

    def __str__(self):
        return self.name

    def temperature_f(self):
        return (self.temperature * 1.8) + 32


class Tea(models.Model):
    name = models.CharField(max_length=512)
    type = models.ForeignKey(TeaType, on_delete=models.SET_NULL, null=True)
    barcode = models.CharField(max_length=512, blank=True, default="")
    in_stock = models.BooleanField(default=False)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tea = models.ForeignKey(Tea, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} loves {self.tea}"
