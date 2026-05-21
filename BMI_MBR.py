def bereken_gezondheid(gewicht, lengte_cm, leeftijd, geslacht):
    # 1. Bereken BMI (lengte moet in meters)
    lengte_m = lengte_cm / 100
    bmi = gewicht / (lengte_m ** 2)
    
    # 2. Bereken BMR op basis van geslacht
    if geslacht.lower() == 'man':
        bmr = 88.362 + (13.397 * gewicht) + (4.799 * lengte_cm) - (5.677 * leeftijd)
    else:
        bmr = 447.593 + (9.247 * gewicht) + (3.098 * lengte_cm) - (4.330 * leeftijd)
        
    return round(bmi, 1), round(bmr, 0)

# Test de werking in de console
if __name__ == "__main__":
    print("--- Test Gezondheid Calculator ---")
    test_gewicht = float(input("Voer gewicht in (kg): "))
    test_lengte = float(input("Voer lengte in (cm): "))
    test_leeftijd = int(input("Voer leeftijd in (jaren): "))
    test_geslacht = input("Voer geslacht in (man/vrouw): ")

    resultaat_bmi, resultaat_bmr = bereken_gezondheid(test_gewicht, test_lengte, test_leeftijd, test_geslacht)

    print(f"\nResultaten:")
    print(f"Je BMI is: {resultaat_bmi}")
    print(f"Je BMR (dagelijkse caloriebehoefte in rust) is: {resultaat_bmr} kcal")