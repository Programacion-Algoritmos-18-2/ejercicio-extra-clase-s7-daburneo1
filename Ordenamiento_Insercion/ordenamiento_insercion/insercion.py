class OrdenamientoInsercion (object):

	def __init__(self, datos):
		self.data = datos

	def Ordenar (self):

		insercion = 0 #variable temporal

		siguiente = 1 #Se define siguiente en 1 para ser utilizado en el for para que recorra desde la posicion 1 del arreglo

		for siguiente in range(0,len(self.data)): #Se define el rango que debe recorrerse el arreglo

			insercion = self.data[siguiente] #almacena el valor 

			moverElemento = siguiente #inicializa la ubicacion para colocar el elemento

			#Encargado de buscar el lugar correspondiente al elemento seleccionado
			while(moverElemento) > 0 and (self.data[moverElemento -1] > insercion):
				#Desplaza el elemento una posicion a la derecha
				self.data[moverElemento] = self.data[moverElemento-1]
				moverElemento = moverElemento - 1
			#Coloca el elemento en la posicion correspondiente
			self.data[moverElemento] = insercion

		return self.data