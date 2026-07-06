import funciones

def menuPrincipal():
    print("\t\t...::::: M E N U   P R I N C I P A L :::::...\n")
    opcion=input("\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\t4.- Mostrar\n\t5.- Buscar\n\t6.- Limpiar\n\t7.- Salir\n\tEscribe una opción: ").strip()
    return opcion


def agregarPeliculas(pelis):
    print("\t\t...::::: AGREGAR CARACTERISTICA A UNA PELICULA :::::...\n")
    caracteristica=input("Ingresa la caracteristica: ").upper().strip()
    valor=input("Ingresa el valor: ").upper().strip()

    pelis[caracteristica]=valor
    funciones.accionExitosa()


def mostrarPeliculas(pelis):
    print("\t\t...::::: MOSTRAR  CARACTERISTICA DE LA PELICULA :::::...\n")
    if len(pelis)>0:
        print("\tCaracteristica\tValor")
        for i in pelis:
            print(f"\t{i}\t\t{pelis[i]}")
    funciones.espereTecla()


def limpiarPeliculas(pelis):
    print("\t\t...::::: BORRAR TODAS LAS CARACTERISTICAS DE LAS PELICULAS :::::...\n")
    if len(pelis)>0:
        opc=input("¿Deseas borrar TODAS las peliculas (Si/No)? ").lower().strip()
        while opc!="si" and opc!="no":
            opc=input("¿Deseas borrar TODAS las peliculas (Si/No)? ").lower().strip()
        if opc=="si":
            pelis.clear()
            funciones.accionExitosa()
    else:
        input("\n\t...¡No existen peliculas que borrar, verifique! ....")


def buscarPeliculas(pelis):
    print("\t\t...::::: BUSCAR CARACTERISTICA DE LA PELICULA :::::...\n")
    caracteristica=input("Escribe la caracteristica de la pelicula: ").upper().strip()
    print("\tCaracteristica\tValor")
    noencontro=True
    for i in pelis:
        if caracteristica==i:
            print(f"\t{i}\t\t{pelis[i]}")
            noencontro=False
    funciones.espereTecla()
    if noencontro:
        input("\n\t...¡NO existe esta caracteristica, no existe!")


def borrarPeliculas(pelis):
    print("\t\t...::::: BORRAR  CARACTERISTICA PELICULAS :::::...\n")
    caracteristica=input("Escribe el nombre de la Caracteristica: ").upper().strip()
    noencontro=True
    for i in list(pelis):
        if caracteristica==i:
            opc=""
            while opc!="si" and opc!="no":
                opc=input("¿Deseas borrar la caracteristica (Si/No)? ").lower().strip()
            if opc=="si":
                pelis.pop(i)
                funciones.accionExitosa()
            noencontro=False
    if noencontro:
        input("\n\t...¡No existe la caracteristica que andas buscando!...")


def modificarPeliculas(pelis):
    print("\t\t...::::: MODIFICAR LAS CARACTERISTICAS PELICULAS :::::...\n")
    peli=input("Escribe el nombre de la Caracteristica: ").upper().strip()
    noencontro=True
    if peli in pelis:
        opc=""
        while opc!="si" and opc!="no":
            opc=input("¿Deseas modificar la caracteristica (Si/No)? ").lower().strip()
        if opc=="si":
            pelis[peli]=input("Escribe el nuevo valor: ").upper().strip()
            funciones.accionExitosa()
        noencontro=False
    if noencontro:
        input("\n\t...¡No existe la caracteristica que andas buscando!...")


def buscarpeliculas2(pelis):
    print("\t\t...::::: BUSCAR CARACTERISTICAS DE LAS PELICULAS :::::...\n")
    caracteristica=input("Escribe el nombre de la caracteristica: ").upper().strip()

    noencontro=True
    print("\tCaracteristica\tValor")
    for i in pelis:
        if caracteristica==i:
            print(f"\t{i}\t\t{pelis[i]}")
            noencontro=False
    funciones.espereTecla()
    if noencontro:
        input("\n\t...¡NO existe esta caracteristica que andas buscando!...")