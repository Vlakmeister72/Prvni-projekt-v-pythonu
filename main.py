print("Hello World!", 69) # Pokud chci víc datovýh typů, musím oddělit čárkou ","

# Vytvoření proměnné (deklarace/inicializace)
cislo = 69 # Do proměnné cislo je uložena hodnota 69: datový typ Int

print("Druhý způsob s proměnnou", cislo)

# Vytvoření proměnné s uloženým textem
text = "Zde je v proměnné uložený text"

# Do konzole vypisujeme obě proměnné, oddělujeme čárkou
print(text, cislo)

# Vytvoření vstupní hodnoty, uživatel musí zadat hodnotu do terminálu
# následně se hodnota zadaná do terminálu uloží do proměnné
vstupni_promenna = input() # input() - Příkaz pro vstupní data

# input () do závorek zapisujeme přidanou hodnotu uživatele

druha_vstupni_promenna = input("Zadejte číslo: ")

# print() nám vypíše do konzole, co uživatel zadal do inputu
print(vstupni_promenna, druha_vstupni_promenna)