"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Petr Vajgl  
email: petervajgl@seznam.cz
"""
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',

    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',

    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

user = {"bob", "ann", "mike", "liz"}
user_password = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
cara = "-" * 40

username = input("username: ")
password = input("password: ")
print(cara)

if username in user_password and user_password[username] == password:
    print(f"Welcome to the app, {username}.")
    print("We have 3 texts to be analyzed.")
else:
    print("Unregistered user, terminating the program..")
    exit()
print(cara)

selection = input("Enter a number btw. 1 and 3 to select: ")
if not selection.isdigit() or not (1 <= int(selection) <= 3):
    print("Neplatný výběr.")
    exit()

selected_text = TEXTS[int(selection) - 1]

words = selected_text.split()
cleaned_words = [word.strip(".,:;!?") for word in words]

total_words = len(cleaned_words)
titlecase_words = sum(1 for word in cleaned_words if word.istitle())
uppercase_words = sum(1 for word in cleaned_words if word.isupper())
lowercase_words = sum(1 for word in cleaned_words if word.islower())
numeric_strings = [word for word in cleaned_words if word.isdigit()]
numeric_count = len(numeric_strings)
numeric_sum = sum(int(num) for num in numeric_strings)

print("-" * 40)
print(f"There are {total_words} in the selected items.")
print(f"There are {titlecase_words} titlecase words.")
print(f"There are {uppercase_words} uppercase words.")
print(f"Trere are {lowercase_words} lowercase words.")
print(f"There are {numeric_count} numeric strings.")
print(f"The sum of all the numbers {numeric_sum}")
print("-" * 40)

lengths = {}
for word in cleaned_words:
    length = len(word)
    lengths[length] = lengths.get(length, 0) + 1

print(" LEN|  OCCURENCES  |NR.")
print("-" * 20)
for length in sorted(lengths):
    stars = '*' * lengths[length]
    print(f"{length:>6} | {stars} ({lengths[length]})")
