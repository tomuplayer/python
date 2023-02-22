
#Kerrotaan että numero "summa" on alussa numero "0"
summa = 0


#Tervehdys- viesti
print("------------------------------------------------")
print("       <+---Tervetuloa laskin.1.0:aan---+>")
print("------------------------------------------------")
print("")
print("")

#Ensimmäinen kysymys
print("[--------+=Lisää haluamasi vaihtoehto=+--------]")
print("|--------1--------Pluslasku----------1--------|")
print("|--------2-------Miinuslasku---------2--------|")
print("|--------3--------Jakolasku----------3--------|")
print("|--------4--------Kerolasku----------4--------|")
print("[--------5--------+=POISTU=+---------5--------]")
print("")
#Valitse kysymys
kys1 = input("Minkä vaihtoehdon valitset? : ")
print("")

#Pluslaskun- funktio
if kys1 == "1":
    while True:
        #Printataan laskuvaihtoehdot
        print("[---------------)Pluslasku(-------------]")
        print("[-----------1-----Numero-----1----------]")
        print("[-----------2------Summa-----2----------]")
        print("[-----------3-----Lopeta-----3----------]")
        print("[---------------)Pluslasku(-------------]")

        kys2 = input("Minkä vaihtoehdon valitset? : ")

        #Kysytään käyttäjältä numeroa
        if kys2 == "1":
            numero = input("Anna numero : ")
            summa += int(numero)
            
        #Lopetetaan "while" looppi
        if kys2 == "3":
            break
        
        #Printataan "summa" ja kysytäänkö lopetetaanko "while" looppi
        if kys2 == "2":
            print("--------------")
            print("Summa:", summa)
            print("--------------")
            kys3 = input("Haluatko jatkaa laskemista?(k/e) : ")
            if kys3 == "e":
                break


#Miinuslaskun- funktio
if kys1 == "2":
    while True:
        #Printataan laskuvaihtoehdot
        print("[--------------)Miinuslasku(------------]")
        print("[-----------1-----Numero-----1----------]")
        print("[-----------2------Summa-----2----------]")
        print("[-----------3-----Lopeta-----3----------]")
        print("[--------------)Miinuslasku(------------]")

        kys2 = input("Minkä vaihtoehdon valitset? : ")

        #Kysytään käyttäjältä numeroa
        if kys2 == "1":
            numero = input("Anna numero : ")
            summa -= int(numero)

        #Lopetetaan "while" looppi
        if kys2 == "3":
            break
        
        #Printataan "summa" ja kysytäänkö lopetetaanko "while" looppi
        if kys2 == "2":
            print("--------------")
            print("Summa:", summa)
            print("--------------")
            kys3 = input("Haluatko jatkaa laskemista?(k/e) : ")
            if kys3 == "e":
                break


#Jakolaskun- funktio
if kys1 == "3":
    while True:
        #Printataan laskuvaihtoehdot
        print("[--------------)Jakolasku(--------------]")
        print("[-----------1-----Numero-----1----------]")
        print("[-----------2------Summa-----2----------]")
        print("[-----------3-----Lopeta-----3----------]")
        print("[--------------)Jakolasku(--------------]")

        kys2 = input("Minkä vaihtoehdon valitset? : ")

        #Kysytään käyttäjältä numeroa
        if kys2 == "1":
            numero = input("Anna numero : ")
            summa /= int(numero)

        #Lopetetaan "while" looppi
        if kys2 == "3":
            break
        
        #Printataan "summa" ja kysytäänkö lopetetaanko "while" looppi
        if kys2 == "2":
            print("--------------")
            print("Summa:", summa)
            print("--------------")
            kys3 = input("Haluatko jatkaa laskemista?(k/e) : ")
            if kys3 == "e":
                break

#Kertolaskun- funktio
if kys1 == "3":
    while True:
        #Printataan laskuvaihtoehdot
        print("[--------------)Kertolasku(-------------]")
        print("[-----------1-----Numero-----1----------]")
        print("[-----------2------Summa-----2----------]")
        print("[-----------3-----Lopeta-----3----------]")
        print("[--------------)Kertolasku(-------------]")

        kys2 = input("Minkä vaihtoehdon valitset? : ")

        #Kysytään käyttäjältä numeroa
        if kys2 == "1":
            numero = input("Anna numero : ")
            summa /= int(numero)

        #Lopetetaan "while" looppi
        if kys2 == "3":
            break
        
        #Printataan "summa" ja kysytäänkö lopetetaanko "while" looppi
        if kys2 == "2":
            print("--------------")
            print("Summa:", summa)
            print("--------------")
            kys3 = input("Haluatko jatkaa laskemista?(k/e) : ")
            if kys3 == "e":
                break