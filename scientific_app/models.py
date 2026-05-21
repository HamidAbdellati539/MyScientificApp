from django.db import models

class HealthCalculation(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    gewicht = models.FloatField()
    lengte_cm = models.FloatField()
    leeftijd = models.IntegerField()
    geslacht = models.CharField(max_length=10)
    bmi = models.FloatField()
    bmr = models.FloatField()

    def __str__(self):
        return f"Meting {self.date.strftime('%Y-%m-%d')} - BMI: {self.bmi}"