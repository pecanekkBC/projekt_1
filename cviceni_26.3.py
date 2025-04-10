cislo_1 = 3.0
cislo_2 = 2.0
if cislo_1 > cislo_2:
    print("První číslo je větší, než druhé")
else:
    if cislo_1 < cislo_2:
        print("První číslo je menší, než druhé")
if cislo_1 == cislo_2:
    print("Obě čísla jsou stejná")


cislo = input("vlož číslo")
if cislo % 3 == 0 and cislo %5== 0:
    print("Fizz Buzz")
elif cislo % 3 == 0:
    print("Fizz")
elif cislo % 5 == 0:
    print("BUZZ")
if cislo % 3 == 0 % 5 ==0:
    print(cislo)