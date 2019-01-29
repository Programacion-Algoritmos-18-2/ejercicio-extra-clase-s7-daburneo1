from ordenamiento_insercion.insercion import * #Se importan las clases empleadas

valores = [10, 90, 1, 20, 4, 7, 40, 27, 22, 50, 47, 3, 5, 18, 21, 28] #Se define el arreglo de valores a ordenar
print("La lista desordenada es:")
print(valores) #Se imprime la lista desordenada

o = OrdenamientoInsercion(valores) #Se envia el arreglo a la clase encargada de realizar el ordenamiento
print("La lista ordenada es: ")
print(o.Ordenar()) #Imrprime la lista ordenada que se retorno del metodo Ordenar 