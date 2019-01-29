class Modelo (object):

    def __init__(self, n, ap, ed):
        # nuevos atributos
        self.nombre = n
        self.apellido = ap
        self.edad = int(ed)

    def agregar_nombre(self, n):
        self.nombre = n
    
    def obtener_nombre(self):
        return self.nombre

    def agregar_apellido(self, ap):
        self.apellido = ap

    def obtener_apellido(self):
        return self.apellido
    
    def agregar_edad(self, ed):
        self.edad = int(ed)

    def obtener_edad(self):
        return self.edad

def merge_sort(lista): #Metodo de ordenamiento por combinacion
    
    if len(lista) < 2:
        return lista
    else:
        middle = len(lista) // 2
        right = merge_sort(lista[:middle])
        left = merge_sort(lista[middle:])
        return merge(right, left)

def merge(lista1, lista2):

    i, j = 0, 0 
    result = [] 

    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            result.append(lista1[i])
            i += 1
        else:
            result.append(lista2[j])
            j += 1

    result += lista1[i:]
    result += lista2[j:]


    return result




