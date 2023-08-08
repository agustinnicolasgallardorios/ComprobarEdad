insertar_val = int(input("inserte una edad: "))

log = "La edad de Agustin, es 12, y la de nacho, 13"
agustin = 12
nacho = 16

if agustin < insertar_val and nacho > insertar_val:
    print(log)
    print("la edad insertada es mayor a la de agustin, pero menor a la de nacho")
elif agustin > insertar_val and nacho > insertar_val:
    print(log)
    print("la edad insertada es menor a la de agustin, y nacho")
elif agustin < insertar_val and nacho < insertar_val:
    print(log)
    print("la edad insertada es mayor a la de agustin y nacho")
elif agustin > insertar_val and nacho < insertar_val:
    print(log)
    print("la edad insertada, es mayor a la de agustin, pero menor a la de nacho")
    
men = float(input(" "))
