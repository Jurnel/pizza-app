# Willkommen zu meinem Rezept-Programm!
# Hier ist ein einfaches Rezept für einen Schokoladenkuchen:
def schokoladenkuchen():
    zutaten = {
        "Mehl": "250g",
        "Zucker": "200g",
        "Kakaopulver": "50g",
        "Backpulver": "1 TL",
        "Eier": "3",
        "Milch": "200ml",
        "Butter": "100g",
        "Vanillezucker": "1 Päckchen"
    }
    
    print("Zutaten für den Schokoladenkuchen:")
    for zutat, menge in zutaten.items():
        print(f"{zutat}: {menge}")
    
    print("\nZubereitung:")
    print("1. Heize den Ofen auf 180°C vor.")
    print("2. Mische die trockenen Zutaten in einer Schüssel.")
    print("3. Füge die Eier, Milch und geschmolzene Butter hinzu und verrühre alles gut.")
    print("4. Gieße den Teig in eine gefettete Backform.")
    print("5. Backe den Kuchen für etwa 30-35 Minuten.")
    print("6. Lass den Kuchen abkühlen und genieße ihn!")