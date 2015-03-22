# /usr/env/bin python
# enconding:utf-8
#RIVERA PEREZ JOEL NAHIM
#joel.nahim.rivera.perez@gmail.com
import random, itertools
import os, time

#clase que va a heredar de object que es una clase basica
class juegoDeLaVida(object):

	##meteodo "contructor"
	def __init__(self, filas, columnas):
		self.filas = filas
		self.columnas = columnas
		#lambda es una funcion que ejecuta lo que le ingreses, es para ahorra espcaio
		#0 es muerte 1 es vida
		fila_vida = lambda: [random.randint(0,1) for n in range(self.columnas)]
		#fila_vida devuelve una lista con vida aleatoria
		
		
		#comprencion de lista para el final
		self.juego = [fila_vida() for n in range (self.filas)]
	#este metodo se imprimira cada vez que se llame al objeto
	#es mas que nada para redefinir el metodo que se debe ejecutar
	def __str__(self):
		#"tablero" del juego
		juego = ''
		
		for fila in self.juego:
			for celula in fila:
				juego += "." if celula else ' '
			juego += '\n'
		return juego
	#para buscar celulas vecinas
	#primera incidencia juego[0][0]
	def vecinos(self,numeroFilas,numeroColumnas):
		#lista con tuplas, con coordenadas de los vecinos distantes
		
		#distanciaEntreVecinos = [(-1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1)]
		#manera guay
								#lo mandamos a una lista
								#Set, lo transforma en un objeto iterable, tiene la propiedad de que los conjuntos no puede ser repetidos 
								#recibe la lista que va a permutar
		distanciaEntreVecinos = list(set(itertools.permutations([-1,-1,1,1,0],2)))
		
					#x fila y columna 
									#si x esta dentro del numero de filas
															#si y esta dentro del numero de columnas
									#Todo esto devolvera un true
									#por eso negamos
		bordesJuego = lambda x, y: not (x in range(self.filas) and y in range(self.columnas))
		#recorre la lista de tuplas, se desempaquetan las tuplas
		
		vecinos = 0
		
		for distancia_fila, distancia_columna in distanciaEntreVecinos:
			#si no es un borde
			if not bordesJuego(numeroFilas + distancia_fila, numeroColumnas + distancia_columna):
				#si esta vivo anexa un vecino, en caso contrario nada
				vecinos += 1 if self.juego[numeroFilas + distancia_fila][numeroColumnas + distancia_columna] else 0
			continue
		return vecinos
	
	
	def recorrer (self):
		for numeroFilas in range(self.filas):
			for numeroColumnas in range(self.columnas):
				vecinos = self.vecinos(numeroFilas,numeroColumnas)
				
				if vecinos < 2 or vecinos > 3:
					self.juego[numeroFilas][numeroColumnas] = 0 #morir
				elif vecinos == 3:
					self.juego[numeroFilas][numeroColumnas] = 1 #nace o sigue viva
			
	
def main():
	#clear()
	

	print("Bienvenido al juego de la vida")
	print("Por Joel Nahim Rivera Perez")
	filas = input("Filas: ")
	columnas = input("Columnas: ")
	juego = juegoDeLaVida(filas,columnas)
	while True:
		os.system('CLS')
		print juego
		juego.recorrer()
		time.sleep(0.1)
		
main()
#RIVERA PEREZ JOEL NAHIM
#joel.nahim.rivera.perez@gmail.com
