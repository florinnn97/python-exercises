def calculator():
    while True:
        x = float(input("Primul nr: "))
        y = float(input("Al doilea nr: "))
        z = input("Selecteaza operatia: (+, -, *, /) sau 'exit' pentru a iesi: ")

        if z == "exit":
            print("La revedere!")
            break  

        if z == "+":
            rezultat = x + y
        elif z == "-":
            rezultat = x - y
        elif z == "*":
            rezultat = x * y
        elif z == "/":
            if y == 0:
                rezultat = "Eroare: Împărțire la 0!"
            else:
                rezultat = x / y
        else:
            rezultat = "Operație invalidă!"

        print("Rezultatul este:", rezultat)
        continua = input("Vrei să faci altă operație? (da/nu): ").lower()
        if continua != "da":
            print("La revedere!")
            break  

calculator()
