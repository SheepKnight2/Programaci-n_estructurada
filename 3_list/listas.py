print("\033c")

#Ejemplo 1 Crear una lista de numeros e imprimir el contenido
numeros=[10,34,25,45]

print(numeros)

lista="["
for i in numeros:
     lista+=f"{i}, "
print(f"{lista}]")

lista="["
for i in range(0,len(numeros)):
     lista+=f"{numeros[i]}, "
print(f"{lista}]")

lista="["
i=0
while i<len(numeros):
     lista+=f"{numeros[i]}, "
     i+=1
print(f"{lista}]")

#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 

# palabra=["UTD","segundo", "TI","MTI"]
# print(palabra)
# palabra = input("Dame una palabra a buscar: ").strip()

# if palabra in palabra:
#     print("Encontre la palabra en la lista")
# else:
#     print("No encontre la palabra en la lista")

#2DA FORMA
# encontro=False
# for i in range(0,len(palabra)):
#     if i==palabra:
#         encontro=True
# if encontro:
#     print("Encontre la palabra en la lista")
# else:
#     print("No encontre la palabra en la lista")
# #3er FORMA
# encontro=False
# for i in range(0,len(palabra)):
#     if palabra[i]==palabra:
#         encontro=True
# if encontro:
#     print("Encontre la palabra en la lista")
# else:
#     print("No encontre la palabra en la lista")
# #4ta FORMA
# encontro=False
# i=0
# while i<len(palabra):
#     if palabra[i]==palabra:
#         encontro=True
#     i+=1
# if encontro:
#     print("Encontre la palabra en la lista")
# else:
#     print("No encontre la palabra en la lista")



#Ejemplo 3 Añadir elementos a la lista
#Versión 1
lista=[]

true=True
while true:

    dato=input("Ingrese un valor para la lista: ").strip().upper()
    lista.append(dato)
    true=input("¿Deseas añadir más elementos a la lista?(si/no)").lower().strip()
    if true=="no":
        true=False

# Versión 2
true="si"
while true=="si":
    dato=input("Ingrese un valor para la lista: ").strip().upper()
    lista.append(dato)
    true=input("¿Deseas añadir más elementos a la lista?(si/no)").lower().strip()

print(lista)


#Ejemplo 4 Crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda

agenda=[
    ["Carlos", "6181234567"],
    ["Alberto","6182344567"],
    ["Martin","6181231223"],
]
print(agenda)

for i in agenda:
    print(i)


for c in range(0,2):
    for r in range(0,3):
        print(agenda[r][c])

lista=""
for r in range(0,3):
    for c in range(0,2):
        lista+=f"{agenda[r][c]}, "
    lista+="\n"
print("["+lista+"]")
