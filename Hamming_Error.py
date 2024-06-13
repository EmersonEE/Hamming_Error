sumap1 = 0
sumap2 = 0
sumap3 = 0
v_paridad1 = 0
v_paridad2 = 0
v_paridad3 = 0
sumap1e = 0
sumap2e = 0
sumap3e = 0
v_paridad1e = 0
v_paridad2e = 0
v_paridad3e = 0

bitsuma = 0


def obtener_palabra_valida():
    while True:
        informacion = input("Ingrese la informacion en 0 y 1: ")
        if len(informacion) > 4:
            print("informacion Mayor a 4 Bits")
            print("Por favor, ingrese nuevamente.")
        elif all(caracter == "0" or caracter == "1" for caracter in informacion):
            return informacion
        else:
            print("informacion no válida.")
            print("Por favor, ingrese nuevamente.")


# Solicita una informacion válida
informacion = obtener_palabra_valida()

numeros_binarios = ["000", "001", "010", "011", "100", "101", "110", "111"]
# Convierte la palabra en una lista de caracteres
lista = list(informacion)

# lista[0] = 0 A D1
# lista[1] = 1 B D2
# lista[2] = 0 C D3
# lista[3] = 1 D D4
# A B C D
# 0 1 0 1
print(f"El Bit Seleccionado es: {informacion}")

# Paridad 1

if int(lista[0]) == 1:
    sumap1 += 1
    sumap2 += 1

if int(lista[1]) == 1:
    sumap1 += 1
    sumap3 += 1

if int(lista[3]) == 1:
    sumap1 += 1
    sumap2 += 1
    sumap3 += 1

if sumap1 % 2:
    v_paridad1 = 1
else:
    v_paridad1 = 0

# Parida 2
# lista0,lista2,lista3
if int(lista[2]) == 1:
    sumap2 += 1
    sumap3 += 1

if sumap2 % 2:
    v_paridad2 = 1
else:
    v_paridad2 = 0

# Paridad 3
# lista1,lista2,lista3
if sumap3 % 2:
    v_paridad3 = 1
else:
    v_paridad3 = 0

lista_info = [
    str(v_paridad1),
    str(v_paridad2),
    lista[0],
    str(v_paridad3),
    lista[1],
    lista[2],
    lista[3],
]
print(f"Codigo de Hamming: {''.join(lista_info)}")


def obtener_error_valida():
    while True:
        error = input("Ingrese el Bit con Error: ")
        if len(error) > 4:
            print("error Mayor a 4 Bits")
            print("Por favor, ingrese nuevamente.")
        elif all(caracter == "0" or caracter == "1" for caracter in error):
            return error
        else:
            print("Palabra no válida.")
            print("Por favor, ingrese nuevamente.")


error = obtener_error_valida()
lista_error = list(error)
# Paridad 1
if int(lista_error[0]) == 1:
    sumap1e += 1
    sumap2e += 1

if int(lista_error[1]) == 1:
    sumap1e += 1
    sumap3e += 1

if int(lista_error[3]) == 1:
    sumap1e += 1
    sumap2e += 1
    sumap3e += 1

if sumap1e % 2:
    v_paridad1e = 1
else:
    v_paridad1e = 0

# Parida 2
# lista0,lista2,lista3
if int(lista_error[2]) == 1:
    sumap2e += 1
    sumap3e += 1

if sumap2e % 2:
    v_paridad2e = 1
else:
    v_paridad2e = 0

# Paridad 3
# lista1,lista2,lista3
if sumap3e % 2:
    v_paridad3e = 1
else:
    v_paridad3e = 0

lista_info_error = [
    str(v_paridad1e),
    str(v_paridad2e),
    lista_error[0],
    str(v_paridad3e),
    lista_error[1],
    lista_error[2],
    lista_error[3],
]
print(f"Codigo de Hamming: {''.join(lista_info)}")
print(f"Codigo de Hamming Error: {''.join(lista_info_error)}")

# Compuerta XOR
# bit mas significativo paridad 3

xora = bool(v_paridad3) ^ bool(v_paridad3e)
xorb = bool(v_paridad2) ^ bool(v_paridad2e)
xorc = bool(v_paridad1) ^ bool(v_paridad1e)

if xora == True:
    bita = 1
else:
    bita = 0

if xorb == True:
    bitb = 1
else:
    bitb = 0

if xorc == True:
    bitc = 1
else:
    bitc = 0

biterror = [bita, bitb, bitc]
num = "".join(map(str, biterror))


for k in numeros_binarios:
    if k == num:
        break
    else:
        bitsuma += 1

if num == "011":
    num = "100"
else:
    num = num

if bitsuma == 3:
    bitsuma += 1
else:
    bitsuma = bitsuma

if bitsuma == 0:
    print("Su codigo no tiene Errores")
else:
    print(f"Su Error Esta en El Bit: {num}")
    print(f"La Posicion del Error esta en el Bit: {bitsuma}")

if bitsuma == 4:
    lista_error[0] = "1" if lista_error[0] == "0" else "0"
elif bitsuma == 5:
    lista_error[1] = "1" if lista_error[1] == "0" else "0"
elif bitsuma == 6:
    lista_error[2] = "1" if lista_error[2] == "0" else "0"
elif bitsuma == 7:
    lista_error[3] = "1" if lista_error[3] == "0" else "0"

print(f"Su Codigo correcto es: {''.join(lista_error)} ")
