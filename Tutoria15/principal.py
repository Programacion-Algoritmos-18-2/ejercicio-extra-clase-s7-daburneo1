from leer_archivo.archivo import *
from modelado.modelo import *

m = MiArchivo() # abrir el archivo
 
lista = m.obtener_informacion() #obtener la informacion del archivo
lista = [l.split(";") for l in lista] # separar por ;
lista1 = [] # se crea la nueva lista que solo va a almacenar las edades
for d in lista:
	mo = Modelo(d[0], d[1], d[2]) # Se envia la primera lista a Modelo 
	lista1.append(mo.obtener_edad()) # se almacena las edades en el nuevo arreglo mediante el metodo obtener_edad

# se imprime la lista de datos desordenada
print("La lista de edades en desorden es:")
print(lista1)

# se envia al metodo para odrenar
merge_sort_result = merge_sort(lista1)

#Se imprime la lista ordenada
print("\nLa lista de edades ordenadas es:")
print(merge_sort_result)

# cierra el archivo
m.cerrar_archivo()
