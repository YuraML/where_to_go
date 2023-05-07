from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField()
    description_long = models.TextField()
    lng = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images', null=True)
    img = models.ImageField()
    number = models.PositiveIntegerField(db_index=True)

    class Meta:
        ordering = ['number']

    def __str__(self):
        return f"{self.id} {self.place}"
