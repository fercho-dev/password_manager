from hashlib import sha256


ADMIN_PASSWORD = "Your secret admin password"

def create_password(service, admin_pass):
    return sha256(admin_pass.encode('utf-8') + service.lower().encode('utf-8')).hexdigest()[:10]

def get_hex_key(admin_pass, service):
    return sha256(admin_pass.encode('utf-8') + service.lower().encode('utf-8')).hexdigest()

def get_password(admin_pass, service):
    return create_password(service, admin_pass)

def add_password(service, admin_pass):
    return create_password(service, admin_pass)


print("\n"+ "*"*15)
print("Comandos:")
print("s = salir del programa")
print("oc = obtener contraseña")
print("gc = generar contraseña")
print("*"*15)

connect = ""

while connect != ADMIN_PASSWORD:
    connect = input("\n¿Cuál es tu contraseña de administrador?\n")
    if connect == "s":
        break

if connect == ADMIN_PASSWORD:
    print("\n¡Bienvenido! ¿Qué deseas hacer?\n")
    
    while True:
        input_ = input(":")

        if input_ == "s":
            break
        if input_ == "gc":
            service = input("¿Cuál es el nombre del servicio?\n")
            print("\n" + "La contraseña creada para " + service.capitalize() + " es:\n" + add_password(service, ADMIN_PASSWORD))
        if input_ == "oc":
            service = input("\n¿Cuál es el nombre del servicio?\n")
            print("\n" + "Tu contraseña de " + service.capitalize() + " es:\n" + get_password(ADMIN_PASSWORD, service))
