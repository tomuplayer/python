#Moduulit
import datetime
import calendar
import random

printteri = False
#Aloitus viesti
print("*" * 31)
print("    Tervetuloa printteriin!")
print("*" * 31)

#Ensimmäinen kyysymys
kysymys0 = input("Haluatko käyttää printteriä? (kyllä/ei) : ")

if kysymys0 == "ei" : 
    printteri = False
    print("Näkemiin!")


if kysymys0 == "kyllä" :
    printeri = True
    
kysymys1 = input("Mitä haluat printata? : ")


#Kysymys "lista" 
if kysymys1 == "lista" :
    print("Voit printata : kaleneri  numero  sana  ")
#Kalenteri vaihtoehto
if kysymys1 == "kalenteri" : 
    vuosi = int(input("Mikä vuosi? : "))
    kuukausi = int(input("Mikä kuukausi? : "))
    print("*" * 25)
    print(calendar.month(vuosi, kuukausi))
    print("*" * 25)
#Numero vaihtoehto
if kysymys1 == "numero" :
    numerokysymys = input("Haluatko oman numeron vai random numeron? (random/oma) : ")
    if numerokysymys == "random" :
        randomnumero = random.randint(0, 100)
        print(randomnumero)
    if numerokysymys == "oma" :
        numerokysymys2 = int(input("Minkä numeron haluat printata? : "))
        print("*" * 4)
        print(numerokysymys2)
        print("*" * 4)
#Kysymys sana
if kysymys1 == "sana" :
    sanakysymys = input("Minkä sanan haluat tulostaa? : ")
    print("*" * 50)
    print(sanakysymys)
    print("*" * 50)



