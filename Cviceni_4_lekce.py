muj_slovnik = {}
kontakty = {"mobil": "+420582582582", "email": "matous@matous.cz" }
muj_slovnik["kontakt"] = kontakty
print(muj_slovnik["kontakt"])
print(muj_slovnik["kontakt"]["mobil"])
print(muj_slovnik["kontakt"]["email"])
cara =("==="* 147)
print(cara)

# testování setů 
muj_set = {"zena", "ruze", "pisen", "kost"}
print(type(muj_set))

prvni_set = set()
print(type(set))

druhy_set = {"predseda", "soudce"}
print(type(druhy_set))

print(cara)
muj_list = ["mesto", "more", "kure", "staveni"]
muj_tupl = ("pan", "hrad", "muz", "stroj")

treti_set = set(muj_list)
ctvrty_set = set(muj_tupl)

print(type(treti_set))
print(type(ctvrty_set))

print(cara)
set_a = {"zena", "ruze", "kost", "pisen", "Lucie", "Matous"}
set_b = {"zena", "ruze", "kost", "pisen", "Lukas"}
print(set_a.union(set_b))
print(set_a.intersection(set_b))
print(set_a.symmetric_difference(set_b))
print(set_a.difference(set_b))
print(cara)

set_a = {"zena", "ruze", "kost"}
set_a.add("pisen")
set_a.update(("matouš", "lucie"))
print(set_a)
print(cara)

set_a = {"zena", "ruze", "Matous", "Lucie"}
set_a.discard("Matous")
print(set_a)

print(cara)


