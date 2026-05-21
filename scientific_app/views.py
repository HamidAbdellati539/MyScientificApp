from django.shortcuts import render
from .models import HealthCalculation

def health_calculator_view(request):
    bmi_result = None
    bmr_result = None
    
    # Controleer of de gebruiker het formulier heeft verstuurd (POST-request)
    if request.method == "POST":
        # Haal de inputs op uit het formulier
        gewicht = float(request.POST.get('gewicht'))
        lengte_cm = float(request.POST.get('lengte'))
        leeftijd = int(request.POST.get('leeftijd'))
        geslacht = request.POST.get('geslacht')
        
        # 1. Bereken de BMI
        lengte_m = lengte_cm / 100
        bmi_result = round(gewicht / (lengte_m ** 2), 1)
        
        # 2. Bereken de BMR (Harris-Benedict formule)
        if geslacht == 'man':
            bmr_result = round(88.362 + (13.397 * gewicht) + (4.799 * lengte_cm) - (5.677 * leeftijd), 0)
        else:
            bmr_result = round(447.593 + (9.247 * gewicht) + (3.098 * lengte_cm) - (4.330 * leeftijd), 0)
            
        # 3. Sla de berekening op in de SQLite database (zoals gevraagd in de opgave)
        HealthCalculation.objects.create(
            gewicht=gewicht,
            lengte_cm=lengte_cm,
            leeftijd=leeftijd,
            geslacht=geslacht,
            bmi=bmi_result,
            bmr=bmr_result
        )

    # Haal álle eerdere berekeningen op uit de database om te tonen in een tabel (geschiedenis)
    geschiedenis = HealthCalculation.objects.all().order_by('-date')

    # Geef de resultaten en de geschiedenis mee aan de HTML-template
    context = {
        'bmi': bmi_result,
        'bmr': bmr_result,
        'history': geschiedenis
    }
    
    return render(request, 'scientific_app/calculator.html', context)