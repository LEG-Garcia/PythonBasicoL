'''
Hoja de trabajo dos
Nombre: Lucía García

'''

# ejercicio uno

print("----------------------- Ejercicio uno -----------------------")

priemraContraseña  = input("Ingrese una contraseña : ")
segundaContraseña= input("¿Por favor de ingresar de nuevo su contraseña? ")

if priemraContraseña == segundaContraseña:
    print("La contraseña si coincide")
elif priemraContraseña != segundaContraseña:
    print("La contraseña no coincide")

print("-------------------------------------------------------------")

# Ejercicio 2

print("------------------- Ejercicio dos ---------------------------")

nombre = input(" Ingrese su nombre : ")
sexo   = input(" Ingrese su sexo F/M: ")

leerInicialNombre = nombre[0].upper() 
leerIncialSexo    = sexo[0].upper()

abecedario = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

nombreInicial = leerInicialNombre
sexoInicial = leerIncialSexo

print("--***************************--")

for x in abecedario:
    for y in nombreInicial:
        if  x >= 'A' and x <= 'L':
            if x == y and  sexoInicial == 'F':
                print(nombre ,"pertenece al grupo A ")
            elif x == y and  sexoInicial == 'M':
              print(nombre,"pertenece al grupo B ")
            break  
        elif x >= 'O' and x <= 'Z':
            if x == y and  sexoInicial == 'M':
                print(nombre, "pertenece al grupo A ")
            elif x == y and  sexoInicial == 'F':
              print(nombre, "pertenece al grupo B")
            break 
        elif x == 'M' or x == 'N':
            if x == y :
                print(nombre, "pertenece al grupo B ")
                break

print("-------------------------------------------------------------")