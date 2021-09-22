from django.db import models


class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateTimeField(blank=False, null=False)
    name = models.TextField(blank=False, null=False)
    count = models.IntegerField(blank=False, null=False)
    distance = models.FloatField(blank=False, null=False)

    def _str_(self):
        return self.name


