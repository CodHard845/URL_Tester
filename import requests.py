import requests

url = input("Entre l'url a tester (avec préfixe http/s): ")

try:
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
        print(f"{url} est accessible.")
    else:
        print(f"{url} a répondu avec le code {response.status_code}")
except requests.RequestException:
    print(f"{url} est hors ligne ou inaccessible.")