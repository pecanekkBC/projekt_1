mesta = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]

ceny = (150, 200, 120, 120, 100, 180)

slevy = ("Olomouc", "Svitavy", "Ostrava")

domeny = ("gmail.com", "seznam.cz", "email.cz")

dvojita_cara = "=" * 35
cara = "-" * 35

nabidka = """
1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180
"""

AKT_ROK = 2025

print("VITEJTE U NASI APLIKACE DESTINATIO!")
print(dvojita_cara, end='')
print(nabidka, end='')
print(dvojita_cara)

destinace_cislo = int(input("VYBER ČÍSLO DESTINACE: "))

if destinace_cislo >= 1 and destinace_cislo <= 6:
    destinace_nazev = mesta[destinace_cislo -1]
    print("Destinace: " + destinace_nazev.upper())
else:   
    print("Destinace číslo: " + str(destinace_cislo) +" NEEXISTUJE ")
    quit()
print(cara)

if destinace_nazev in slevy:
    nova_cena = 0.75 * ceny[destinace_cislo - 1]
    print("Získáváte slevu 25%! Nová cena je: " + str(nova_cena) + ",- ")
else:
    nova_cena = ceny[destinace_cislo - 1]
    print("Cena jizdeny je bez slevy. Cena: " + str(nova_cena) + ",- " )

print(cara)

cele_jmeno = input("Vaše celé jméno: ")
krestni_jmeno = cele_jmeno.split()[0]

if krestni_jmeno.isalpha():
    print("Vaše křestni jméno je: ", krestni_jmeno)
else:
    print("Neplatné jméno!")
print(cara)

rok_narození = int(input("Zadejte Váš rok narození: "))

if (AKT_ROK - rok_narození) >= 18:
    print("Přístup povolen!")
else:
    print("Jste moc mladá/ý na nákup jízdenek!")
    print("Ukončuji program")
    quit()
print(cara)

email = input("Zapiš Vaši emailovou adresu: ")
if "@" in email and email.split("@")[1] in domeny:
    print("Ověření emailu proběhlo úspěšně! ")
else:
    print("Tento mail je neplatný!")
    print("Ukončuji program")
    quit()
print(dvojita_cara)

print(
    "\nDěkuji, " + krestni_jmeno + " za objednávku jízdenky!" +
    "\nCílová destinace: " + destinace_nazev + ", cena jízdného: " + str(nova_cena) + ",-Kč" + 
    "\nNa Váš email: " + email + " jsme odeslali e-jízdenku, přejeme šťastnou cestu! \n"  
)
print(dvojita_cara * 2)
