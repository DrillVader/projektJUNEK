"""
projektJUNEK.py: první projekt do Engeto Online Python Akademie
author: Vojtěch Junek
email: vojta.junek@tiscali.cz
discord: jsemnamol#8198
"""





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


    



