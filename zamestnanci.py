zamestnanci = ["'František','Anna','Jakub','Klára'"]
print("Zaměstnanci na začátku", zamestnanci)
zamestnanci_a = ["'František','Anna','Jakub','Klára', 'Bruno', 'Aneška'"]
print("Nová jména přidána:", zamestnanci_a)
zamestnanci_b = ["'František','Bruno','Anna','Jakub','Klára'"]
print("Nová jména vložena: ", zamestnanci_b)

# Vytvoření seznamu "zamestnanci"
zamestnanci = ['František', 'Anna', 'Jakub', 'Klára']

# Výpis seznamu "zamestnanci"
print('Zaměstnanci na začátku:', zamestnanci)

# Přidání nových jmen
zamestnanci_a = zamestnanci.copy()
zamestnanci_a.append('Bruno')
zamestnanci_a.append('Anežka')

# Výpis aktualizovaného obsahu "kandidati"
print("Nová jména přidána:", zamestnanci_a)

# Vlož string na index
zamestnanci_b = zamestnanci.copy()
zamestnanci_b.insert(1, "Bruno")

# Výpis seznamu "zamestnanci"
print("Nová jména vložena:", zamestnanci_b)


vstupni_cisla = [1, 2, 3, 4, 5, 6, 7]
vstupni_pismena = ["p", "ú", "s", "č", "p", "s", "n"]
tyden = ('pondělí', 'úterý', 'středa', 'čtvrtek', 'pátek', 'sobota', 'neděle')
cislo_dne = 3
if cislo_dne is vstupni_cisla:
    print("Správná vstupní hodnota!")
