from hashlib import sha256


def create_password(service, master_key):
    return sha256(master_key.encode('utf-8') + service.lower().encode('utf-8')).hexdigest()[:10]

def get_password(master_key, service):
    return create_password(service, master_key)

def add_password(service, master_key):
    return create_password(service, master_key)

print("\n¡Bienvenido! ¿Qué deseas hacer?\n")
print("\n"+ "*"*15)
print("Comandos:")
print("s = salir del programa")
print("oc = obtener contraseña")
print("gc = generar contraseña")
print("*"*15)
    
while True:
    input_ = input(":")

    if input_ == "s":
        break
    if input_ == "gc":
        master_key = input("\n¿Cuál es tu llave maestra?\n")
        service = input("\n¿Cuál es el nombre del servicio?\n")
        print("\n" + "La contraseña creada para " + service.capitalize() + " es:\n" + add_password(service, master_key))
    if input_ == "oc":
        master_key = input("\n¿Cuál es tu llave maestra?\n")
        service = input("\n¿Cuál es el nombre del servicio?\n")
        print("\n" + "Tu contraseña de " + service.capitalize() + " es:\n" + get_password(master_key, service))
