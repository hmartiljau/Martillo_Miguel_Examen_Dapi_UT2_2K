def ListaNombres(lista_de_nombres):
    '''
    Esta función ordena alfabeticamente una lista de nombres
    Parámetros:
        -lista de nombres: Esta lista de nombres guarda una cantidad indeterminada de nombres en este formato:
        ['Nombre Apellido 1', Nombre Apellido 2,..., 'Nombre Apellido N'),
    Salida:
        Lista de nombres: Devuelve la lista de nombres ordenada alfabeticamente
    '''
    lista_de_nombres = lista_de_nombres.split('')
    nombres = {}
    
    if len(nombres) > 0:
        nombres=input('introduce un nombre y apellido')
    else :
        return OrdenarNombre()

def OrdenarNombre(nombreordenado):
    '''
    Esta función recibe un 'nombre y apellido' y devuelve el 'apellido,nombre'.
    Parámetros:
        -Nombre en el formato 'Nombre Apellido'
    Salida:
        -Nombre en el formato 'Apellido Nombre'
    '''
    nombreordenado = nombreordenado.sort()
    return nombreordenado