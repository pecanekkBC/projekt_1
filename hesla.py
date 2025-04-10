oddelovac = "=" * 62

sluzby = ("dostupne filmy", "detaily filmu", 'reziseri', "doporuc film")

uzivatele = {
    "tomas": {"Shawshank Redemption", "The Godfather", "The Dark Knight"},
    "petr": {"The Godfather", "The Dark Knight"},
    "marek": {"The Dark Knight", "The Prestige"}
}

film_1 = {
    "JMENO": "Shawshank Redemption",
    "HODNOCENI": "93/100",
    "ROK": 1994,
    "REZISER": "Frank Darabont",
    "STOPAZ": 144,
    "HRAJI": ("Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler",
      "Clancy Brown", "Gil Bellows", "Mark Rolston", "James Whitmore",
      "Jeffrey DeMunn", "Larry Brandenburg"
     )
}

film_2 = {
    "JMENO": "The Godfather",
    "HODNOCENI": "92/100",
    "ROK": 1972,
    "REZISER": "Francis Ford Coppola",
    "STOPAZ": 175,
    "HRAJI": ("Marlon Brando", "Al Pacino", "James Caan",
      "Richard S. Castellano", "Robert Duvall", "Sterling Hayden",
      "John Marley", "Richard Conte"
    )
}

film_3 = {
    "JMENO": "The Dark Knight",
    "HODNOCENI": "90/100",
    "ROK": 2008,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 152,
    "HRAJI": ("Christian Bale", "Heath Ledger", "Aaron Eckhart",
      "Michael Caine", "Maggie Gyllenhaal", "Gary Oldman", "Morgan Freeman",
      "Monique Gabriela", "Ron Dean", "Cillian Murphy"
    )
}

film_4 = {
    "JMENO": "The Prestige",
    "HODNOCENI": "85/100",
    "ROK": 2006,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 130,
    "HRAJI": ("Hugh Jackman", "Christian Bale", "Michael Caine",
      "Piper Perabo", "Rebecca Hall", "Scarlett Johansson", "Samantha Mahurin",
      "David Bowie"
    )
}

filmy = {
    film_1["JMENO"]: film_1,
    film_2["JMENO"]: film_2,
    film_3["JMENO"]: film_3,
    film_4["JMENO"]: film_4,
}

uzivatel = input("zadej jméno: ")
if not uzivatel in uzivatele:
    print("neregistrovaný uživatel")
    quit()
else:
    print("V POŘÁDKU ", oddelovac, sep="\n")
    print("VÍTEJTE V NAŠEM FILMOVÉM SLOVNÍKU".upper().center(62), oddelovac, sep="\n")
    print(("| " + " | ".join(sluzby) + " |").center(62), oddelovac, sep="\n")

uzivatel = input("Zadej jméno: ")
vyber = input("Vyber službu: ")
if vyber in sluzby and vyber == "dostupne filmy":
    print("Dostupné filmy:", ', '.join(tuple(filmy.keys())), oddelovac, sep="\n")
elif vyber in sluzby and vyber == "detaily filmu":
    print("Dostupné filmy:", ', '.join(tuple(filmy.keys())), sep="\n")
    film = input("Vyber film: ") 
    print(oddelovac, "Film: " + film, filmy.get(film), oddelovac, sep="\n")
elif vyber in sluzby and vyber == "reziseri":
    print("Reziseri:", ', '.join(tuple(filmy.keys())), sep="\n")
    reziseri = {filmy["Shawshank Redemption"]["REZISER"],
                filmy["The Godfather"]["REZISER"],
                filmy["The Dark Knight"]["REZISER"],
                filmy["The Prestige"]["REZISER"]}
    print(f" {"," .join(reziseri)}", oddelovac, sep="\n")
elif vyber in sluzby and vyber == "doporuc film":
    kopie_hodnoceni = uzivatele.copy()
    aktivni_uzivatel = kopie_hodnoceni.pop(uzivatel)
    zbytek_hodnoceni = kopie_hodnoceni

    detaily_prvni_uzivatel = zbytek_hodnoceni.popitem()
    detaily_druhy_uzivatel = zbytek_hodnoceni.popitem()
    jmeno_prvni_uz = detaily_prvni_uzivatel[0]
    jmeno_druhy_uz = detaily_druhy_uzivatel[0]
    hodnoceni_prvni_uz = detaily_prvni_uzivatel[1]
    hodnoceni_druhy_uz = detaily_druhy_uzivatel[1]
    spolecni_prvni_uziv = aktivni_uzivatel.intersection(hodnoceni_prvni_uz)
    spolecni_druhy_uziv = aktivni_uzivatel.intersection(hodnoceni_druhy_uz)

if len(spolecni_prvni_uziv) > len(spolecni_druhy_uziv):
    nejvice_spolecnych = uzivatele[jmeno_prvni_uz]

elif len(spolecni_prvni_uziv) < len(spolecni_druhy_uziv):
    nejvice_spolecnych = uzivatele[jmeno_druhy_uz]

elif len(spolecni_prvni_uziv) == len(spolecni_druhy_uziv):
    nejvice_spolecnych = uzivatele[jmeno_druhy_uz].union(uzivatele[jmeno_prvni_uz])

    print(f"Oblibene filmy akt. uzivatel: {aktivni_uzivatel}")
    print(f"Nejvice spol. oblibenych filmu: {nejvice_spolecnych}")

    navrhy = set(nejvice_spolecnych).difference(aktivni_uzivatel)
    print(f"Navrhuji filmy: {navrhy}" if navrhy else "Nemam pro tebe zadny film")
else:
    print("SLUZBA NENI DOSTUPNA!")



