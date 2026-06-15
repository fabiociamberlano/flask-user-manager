from db import init_db
from service import *

init_db()

while True:
    print("\n1. Inserisci")
    print("2. Lista")
    print("3. Elimina")
    print("4. Esci")

    scelta = input("Scelta: ")

    if scelta == "1":
        nome = input("Nome: ")
        eta = int(input("Età: "))
        crea_persona(nome,eta)

    elif scelta == "2":
        persone = lista_persone()
        for p in persone:
            print(p)

    elif scelta == "3":
        id = int(input("ID da eliminare: "))
        elimina_persona(id)

    elif scelta == "4":
        break
