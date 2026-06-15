import requests

base_url = "http://127.0.0.1:5000/users"

while True:

    print("\n--- MENU ---")
    print("1. Lista utenti (GET)")
    print("2. Crea utente (POST)")
    print("3. Modifica utente (PUT)")
    print("4. Elimina utente (DELETE)")
    print("5. Esci")

    scelta = int(input("Scelta: "))

    if scelta == 1:
        response = requests.get(base_url)
        print(response.json())

    elif scelta == 2:
        nome =input("Nome: ")
        eta = int(input("Età: "))
        data = {
                "nome":nome,
                "eta":eta
                }
        response = requests.post(base_url,json=data)
        print(response.json())

    elif scelta == 3:
        id = input("ID utente: ")
        nome = input("Nuovo nome: ")
        eta = int(input("Nuova età: "))
        data = {
                "nome":nome,
                "eta":eta
               }
        response = requests.put(
                f"{base_url}/{id}",
                json=data
                )
        print(response.json())

    elif scelta == 4:
        id = input("ID utente da eliminare: ")
        response = requests.delete(f"{base_url}/{id}")
        print(response.json())

    elif scelta == 5:
        break

    else:
        print("Scelta non valida")

