jmeno = "Matyáš" # Vytvoení proměnné s datovým typem string
prijmeni = "Bláha" # -||-, proměnné si pojmenováváme bez diakritiky (háčky, čárky, atd.)
vek = 16 # Vytvoření proměnné s datovým typem integer - Celé číslo, nepíšeme do ""
vyska = 1.8 # Vytvoření proměnné s datovým typem float
pohlavi = False , 69 

# Výpis informace pro uživatele co je 1 (True) či 0 (False)
print("Pohlaví 1 (True) - Holka, 0 (False) - Kluk, 0 (False) + 69 - Femboy") # V printu dáváme jednoduchý string
print(jmeno , prijmeni) # Voláme proměnné pro výpis jména a příjmení v jednom řádku, oddělujeme čárkou

# Efektivnější zápis, "efkovej string"
print(f"Je mu {vek} a měří {vyska} metrů.") 
print(f"Pohlaví - {pohlavi}")