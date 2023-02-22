import random
print("[---------------------------------------]")
print("|---+=Tervetuloa ristinolla 1.0:aan=+---|")
print("[---------------------------------------]")


while True:

    lauta = [" " for x in range(9)]

    def piirrä_lauta():
        row1 = "| {} | {} | {} |".format(lauta[0], lauta[1], lauta[2])
        row2 = "| {} | {} | {} |".format(lauta[3], lauta[4], lauta[5])
        row3 = "| {} | {} | {} |".format(lauta[6], lauta[7], lauta[8])

        print()
        print(row1)
        print(row2)
        print(row3)
        print()

    def pelaajan_liike(ikoni):
        if ikoni == "X":
            numero = 1
        elif ikoni == "O":
            numero = 2
        if numero == 1:
            print("Pelaajan {} vuoro.".format(numero))
            choice = int(input("Lisää x kohtaan (1-9): ").strip())
            if lauta[choice - 1] == " ":
                lauta[choice - 1] = ikoni
            else:
                print()
                print("Tämä kohta on jo viety.")
                pelaajan_liike(ikoni)
        else:
            print("Tietokoneen vuoro")
            choice = random.randint(0,8)
            if lauta[choice] == " ":
                lauta[choice] = ikoni
            else:
                pelaajan_liike(ikoni)

    def voitto(ikoni):
        if (lauta[0] == ikoni and lauta[1] == ikoni and lauta[2] == ikoni) or \
        (lauta[3] == ikoni and lauta[4] == ikoni and lauta[5] == ikoni) or \
        (lauta[6] == ikoni and lauta[7] == ikoni and lauta[8] == ikoni) or \
        (lauta[0] == ikoni and lauta[3] == ikoni and lauta[6] == ikoni) or \
        (lauta[1] == ikoni and lauta[4] == ikoni and lauta[7] == ikoni) or \
        (lauta[2] == ikoni and lauta[5] == ikoni and lauta[8] == ikoni) or \
        (lauta[0] == ikoni and lauta[4] == ikoni and lauta[8] == ikoni) or \
        (lauta[2] == ikoni and lauta[4] == ikoni and lauta[6] == ikoni):
            return True
        else:
            return False

    def tasapeli():
        if " " not in lauta:
            return True
        else:
            return False

    while True:
        piirrä_lauta()
        pelaajan_liike("X")
        piirrä_lauta()
        if voitto("X"):
            print("X voittaa!")
            break
        elif tasapeli():
            print("Tasapeli!")
            break
        pelaajan_liike("O")
        if voitto("O"):
            piirrä_lauta()
            print("O voittaa!")
            break
        elif tasapeli():
            print("Tasapeli!")
            break

    lop = input("Lopetetaanko peli?(k/e) : ")
    if lop == "k":
        break
