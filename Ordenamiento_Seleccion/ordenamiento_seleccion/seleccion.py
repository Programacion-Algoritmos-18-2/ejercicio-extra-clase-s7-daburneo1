class OrdenamientoSeleccion (object):

	def __init__(self, datos):
		self.data = datos #Se obtienen los valores de la clase principal

	def Ordenar(self):
		masPequenio = 0 #indice del elemento mas pequeño

		for i in range(0,(len(self.data)-1)): #for padre para recorrer todo el arreglo
			masPequenio = i #primer indicr
			indice = i+1
			for indice in range(indice,len(self.data)): #for anidado para comparar en parejas los valores
				if (self.data[indice] < self.data[masPequenio]): #condicion para modificar el indice
					masPequenio = indice

			self.Intercambiar(i, masPequenio) #Se envia al metodo para realizar el intercambio
		return self.data #Retorna la lista ordenada

	def Intercambiar(self, primero, segundo): #Metodo para intercambiar los valores del arreglo
		temporal = self.data[primero]
		self.data[primero] = self.data[segundo]
		self.data[segundo] = temporal