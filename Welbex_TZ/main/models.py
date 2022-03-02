from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=250)
    amount = models.IntegerField()
    distance = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
