

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
    
    muoto = input("Minkä muodon haluat : ")
    choice = input("Valitse tehätävä (1,2,3,4,5): ")

    # Kysymys
    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Lisää ensimmäinen numero: "))
        num2 = float(input("Lisää toinen numero: "))

        if choice == '1':
            print(num1, "+", num2, "=", float(muoto(num1, num2)))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        elif choise == '5':
            brake
        
        # Pysäytä looppi
        next_calculation = input("Uusi laskutoimitus?? (kyllä/ei): ")
        if next_calculation == "ei":
          break
    
    else:
        print("Virheellinen tulos...")