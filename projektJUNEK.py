"""
projektJUNEK.py: první projekt do Engeto Online Python Akademie
author: Vojtěch Junek
email: vojta.junek@tiscali.cz
discord: jsemnamol#8198
"""






import string
import re
users = {'Bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123',}

print("Vítám vás v našem textovém analyzátoru \npo přihlášení si budete moct vybrat mezi 3 texty ",
"\na my vám o zadaném textu povíme vše co budete potřebovat :)")

username = input('Uživatelské jméno:'.upper())
password = input('Heslo:'.upper())
if users.get(username) == password:   
    print(f'Ahoj, {username}, vítej v aplikaci! Pokračuj...')
else:
    #pokud nesouhlasí   
    print('Uživatelské jméno nebo heslo nejsou v pořádku, ukončuji')

txt_soubor = open("task_template.txt", mode="r")
obsah_txt = txt_soubor.read()
textList = obsah_txt.split(";")
txt_soubor.close()

print("Zadejte prosím číslo 1-3 pro výběr textu, který chcete analyzovat: ")
volba = input()


def pocetslov():
    res = len(re.findall(r'\w+', textList[int(volba)-1]))    
    print("pocet slov v textu je: ",str(res))

pocetslov()

def zacinajiVelkym():
    list1 = []
    for word in textList[int(volba)-1].split():
        
        if word[0].isupper() and word[0].isalpha():
            list1.append(word)
            
    print("pocet slov začínající velkým písmenem je:",len(list1))

zacinajiVelkym()


def jsouVelkym():
    list1 = []
    for word in textList[int(volba)-1].split():
        
        if word.isupper() and word[0].isalpha():
            list1.append(word)
            
    print("pocet slov velkym písmen je: ",len(list1))
    
    
    
    #list1 = []
    #pocet = sum(map(str.isupper, textList[int(volba)-1].split()))
    #print(pocet)
    

jsouVelkym()

def jsoumalym():
    list1 = []
    pocet = sum(map(str.islower, textList[int(volba)-1].split()))
    print("pocet slov malým písmem je:",pocet)
    

jsoumalym()

def cislice():
    list1 = []
    for word in textList[int(volba)-1]:
        for pismeno in word:
            if pismeno.isnumeric():
                list1.append(pismeno)
        
    print("počet číslic v textu je: ",len(list1))

cislice()

def suma():
    vysledek = 0
    for word in textList[int(volba)-1].split():
        if word.isdigit():
            vysledek += int(word)
        
    print("Suma všech čísel je: ", vysledek)
suma()
        








    #list1 = []
    #pomocnylist = []
    #for word in textList[int(volba)-1]:
     #   if word.isnumeric():
     #       list1.append(word)
     #   elif not word.isnumeric():
      #      for pismeno in word:
      #          if pismeno.isnumeric():
      #              pomocnylist.append(pismeno)       
   # print(list1)
   # print(pomocnylist)



    



