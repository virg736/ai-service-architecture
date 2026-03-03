import requests
import time
import sys

API_URL = "http://localhost:8000"

def main():
    print("Vérification du service IA local...")

    try:
        start = time.time()
        response = requests.get(API_URL)
        duration = round((time.time() - start) * 1000, 2)
    except requests.exceptions.RequestException as e:
        print(f"Erreur de connexion : {e}")
        print("CHECK FAILED")
        sys.exit(1)

    if response.status_code != 200:
        print(f"Code HTTP invalide : {response.status_code}")
        print("CHECK FAILED")
        sys.exit(1)

    try:
        response.json()
    except ValueError:
        print("Réponse non valide (JSON attendu)")
        print("CHECK FAILED")
        sys.exit(1)

    print("=================================")
    print("CHECK PASSED - Service opérationnel")
    print(f"Temps de réponse : {duration} ms")
    print("=================================")

    sys.exit(0)

if __name__ == "__main__":
    main()
