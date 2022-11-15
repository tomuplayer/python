import sys
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint 
from pyfiglet import figlet_format

cprint(figlet_format('LASKIN 2.0            ', font='digital'),
       'yellow', 'on_blue', attrs=['bold'])


#Kaksi numeroa
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

#Tuplaa numerot
def multiply(x, y):
    return x * y

#Puolita numerot
def divide(x, y):
    return x / y


print("Valitse tehtävä lisäämällä numero.")
print("1.Summa")
print("2.Erotus")
print("3.Tulo")
print("4.Osamäärä")
print("5.Lopeta laskeminen")

while True:
    # Tehtävä
    choice = input("Valitse tehätävä (1,2,3,4,5): ")

    # Kysymys
    if choice in ('1', '2', '3', '4', '5'):

        if choice == '1':
            num1 = float(input("Lisää ensimmäinen numero: "))
            num2 = float(input("Lisää toinen numero: "))
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            num1 = float(input("Lisää ensimmäinen numero: "))
            num2 = float(input("Lisää toinen numero: "))
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            num1 = float(input("Lisää ensimmäinen numero: "))
            num2 = float(input("Lisää toinen numero: "))
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            num1 = float(input("Lisää ensimmäinen numero: "))
            num2 = float(input("Lisää toinen numero: ")) 
            print(num1, "/", num2, "=", divide(num1, num2))
        
        elif choice == '5':
            varmasti = input("Haluatko varmasti lopettaa? (kyllä ei) : ")
            if varmasti == "kyllä":
                break

        

        # Pysäytä looppi
        next_calculation = input("Uusi laskutoimitus?? (kyllä/ei): ")
        if next_calculation == "ei":
          break
    
    else:
        print("Virheellinen tulos...")