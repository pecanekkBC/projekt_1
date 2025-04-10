mesta = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
ceny = (150, 200, 120, 120, 100, 180)
cara = "=" * 35
nabidka = """
1 - Praha   | 150,-Kč
2 - Viden   | 200,-Kč
3 - Olomouc | 120,-Kč
4 - Svitavy | 120,-Kč
5 - Zlin    | 100,-Kč
6 - Ostrava | 180,-Kč
"""
print("VITEJTE U NASI APLIKACE DESTINATIO!")
print(cara)
print(nabidka)
print(cara)
destinace = input("Zadej číslo destinace: ")
jmeno = input("Zadej jméno: ")
prijmeni = input("Zadej přijmení: ")
email = input("Zadej tvůj email: ")
cilova_stanice = mesta[int(destinace) - 1]
finalni_cena = ceny [int(destinace) - 1]
print(cilova_stanice)
print(finalni_cena, ",-Kč", sep='')

print(cara)
print("Cestující: ", jmeno, prijmeni)
print("Cílová destinace: ", destinace)
print("Cena jízdného: ", finalni_cena, ",-Kč")
print("Odeslali jsme na email: ", email)
print(cara)
