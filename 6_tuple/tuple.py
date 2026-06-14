"""   

  Las tuplas se utilizan para almacenar varios elementos en una sola variable.

   Una tupla es una colección ordenada e inmutable .

   Las tuplas se escriben entre paréntesis.


"""
print("\033c")

# Crear una tupla
frutas = ("manzana", "pera", "uva")

# Mostrar la tupla completa
print("Tupla:", frutas)

# Acceder a un elemento
print("Primer elemento:", frutas[0])

# Recorrer la tupla
for fruta in frutas:
    print(fruta)

# Tupla con diferentes tipos de datos
datos = ("Daniela", 17, 8.5, True)
print("Datos:", datos)