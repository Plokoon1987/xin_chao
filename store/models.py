from django.db import models


class Dish(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    rations = models.PositiveIntegerField()

    price_per_weight = models.FloatField(blank=True)


    class Meta:
        ordering = ('-price_per_weight',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.price_per_gram = self.price / self.weight
        super().save(*args, **kwargs)
