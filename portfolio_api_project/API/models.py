from django.db import models


class Investment(models.Model):
    company = models.CharField(max_length=30)
    quantity = models.IntegerField(null=True)
    cost = models.IntegerField(null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.company


class Updates(models.Model):
    investment = models.ForeignKey(Investment, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)
    cost = models.IntegerField(null=True)
    date = models.DateField()
    date_entered = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.investment)
