"""
projektJUNEK.py: první projekt do Engeto Online Python Akademie
author: Vojtěch Junek
email: vojta.junek@tiscali.cz
discord: jsemnamol#8198
"""
import re
users = {'Bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123',}

print("Vítám vás v našem textovém analyzátoru.")
print("Po přihlášení si budete moct vybrat mezi 3 texty.")
print("My vám o zadaném textu povíme vše co budete potřebovat.")

while True:
    username = input('Uživatelské jméno:'.upper())
    password = input('Heslo:'.upper())

    if users.get(username) == password:
        print(f'Ahoj, {username}, vítej v aplikaci! Pokračuj...')
        break
    else:
        print("Incorrect username or password, please try again.")

txt = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
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

print("Zadejte prosím číslo 1-3 pro výběr textu, který chcete analyzovat: ")
volba_raw = input()    
def check_cisla(vol):
    if int(vol) in (1, 2, 3):
        volba = int(vol)-1
        return volba
    else:
        print("zadejte číslo 1-3")
        exit()

volba = check_cisla(volba_raw)
    

def pocetslov():
    pocet_slov = len(txt[volba].split())
    print("V tomto textu je  ", pocet_slov, " slov.")

pocetslov()

def zacinajiVelkym():
    list1 = []
    for word in txt[volba].split():        
        if word[0].isupper() and word[0].isalpha():
            list1.append(word)
            
    print("pocet slov začínající velkým písmenem je:",len(list1))

zacinajiVelkym()


def jsouVelkym():
    list1 = []
    for word in txt[volba].split():        
        if word.isupper() and word[0].isalpha():
            list1.append(word)
            
    print("pocet slov velkym písmen je: ",len(list1))   

jsouVelkym()

def jsoumalym():    
    pocet = sum(map(str.islower, txt[volba].split()))
    print("pocet slov malým písmem je:",pocet)
    

jsoumalym()

def cislice():
    list1 = []
    for word in txt[volba].split():
        for pismeno in word:
            if pismeno.isnumeric():
                list1.append(pismeno)
        
    print("počet číslic v textu je: ",len(list1))

cislice()

def suma():
    vysledek = 0
    for word in txt[volba].split():
        if word.isdigit():
            vysledek += int(word)
        
    print("Suma všech čísel je: ", vysledek)
suma()


def graf():
    delky_slov = {}
    for word in txt[volba].split():
        if word.isalpha():
            if len(word) in delky_slov:
                delky_slov[len(word)] += 1
            else:
                delky_slov[len(word)] = 1
                
    word_lengths = dict(sorted(delky_slov.items()))
    
    for length, count in word_lengths.items(): 
        print(f"{length:2d}|{'*'* count:<15} {count}")
    
    
    
print("-" * 30)
print("LEN| OCCURENCES|  NR")    
graf()  
print("-" * 30)








   



    



