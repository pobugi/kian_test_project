from django.db import models

class Fruit(models.Model):
    name = models.CharField("Название фрукта", max_length=100)
    description = models.TextField("Описание фрукта")
    calories = models.IntegerField("К-во калорий на 100 г")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Fruit"
        verbose_name_plural = "Fruits"