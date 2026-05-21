from django.contrib import admin
from .models import HealthCalculation

# Dit zorgt ervoor dat je metingen kunt beheren in de browser
admin.site.register(HealthCalculation)