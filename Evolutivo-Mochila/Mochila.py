'''
Implementación de una mochila para el problema de la Mochila (optimización).

Materia de Cómputo Evolutivo, 5to semestre, Facultad de Ciencias, UNAM.

@author Diego Velázquez Trejo

'''
import random
# Conjunto de objetos de la mochila 
from leyendo_datos_mochila import CONJUNTO_OBJETOS


class Mochila:

    # Variable única y compartida por todas las instancias de la clase Mochila 
    Informacion = CONJUNTO_OBJETOS


    # Constructor de la clase
    def __init__(self, conjunto_objetos, capacidad):
        if(len(conjunto_objetos) > 0):
            # Raise an exception 
            raise Exception("El conjunto de objetos tiene que estar vacío")
            
        self.conjunto = conjunto_objetos    # Conjunto de objetos para la mochila
        self.capacidad = capacidad

        # Funciones para determinar el estado de la mochila 
        self.peso = 0          # Se tiene que calcular de manera directa
        self.valor = 0        # Se tiene que calcular de manera directa
        self.promedio_pesos = self.calcula_promedio(1) # Calcular junto con todo el conjunto de información
        self.promedio_valores = self.calcula_promedio(0) # Calcular junto con todo el conjunto de información

    # Función para remover un elemento de la mochila (aleatoriamente)
    def obtiene_elemento(self):
        if(len(self.conjunto) == 0):
            return None
        lista = list(self.conjunto)
        random.shuffle(lista)
        elemento = lista.pop()
        self.conjunto.remove(elemento)     # Ver si es necesario una función shuffle para el set
        # Tenemos que actualizar los pesos y valores de la mochila
        valor_elemento = Mochila.Informacion[elemento][0]
        peso_elemento = Mochila.Informacion[elemento][1]

        self.peso = self.peso - peso_elemento
        self.valor= self.valor - valor_elemento

        return elemento

    # Función para insertar un elemento en la mochila 
    def agrega_elemento(self, elemento):
        # Tenemos que ver si el peso de la mochila es válido junto con el nuevo elemento
        # Extraemos la información del elemento, es decir, su valor y su peso 
        valor_elemento = Mochila.Informacion[elemento][0]
        peso_elemento = Mochila.Informacion[elemento][1]
        if(not self.verifica_elemento(elemento)):
            if(self.peso + peso_elemento <= self.capacidad and not(elemento in self.conjunto)):
                self.conjunto.add(elemento)

                # Tenemos que actualizar los pesos y valores de la mochila
                self.valor += valor_elemento
                self.peso += peso_elemento

                return True

            else:
                return False
        else:
            return False 
    
    # Función para eliminar un objeto de la mochila en donde le pasamos como argumento el identificador del objeto por eliminar 
    def elimina_elemento(self, elemento):
        if(self.verifica_elemento(elemento)):
            self.conjunto.remove(elemento)
            # Tenemos que actualizar los pesos y valores de la mochila
            self.valor -= Mochila.Informacion[elemento][0]
            self.peso -= Mochila.Informacion[elemento][1]

    # Función para mostrar los elementos de la mochila
    def toString(self):
        return "Capacidad: {c}, #Elemetos: {e}, Peso: {p}, Valor:{v} : ".format(c = self.capacidad ,e = len(self.conjunto), p = self.peso, v = self.valor)+str(self.conjunto)

    # Función para obtener la longitud de la mochila
    def longitud(self):
        return len(self.conjunto)

    # Función para regresar una lista con los identificadores de la mochila 
    def lista_elementos(self):
        return list(self.conjunto)

    # Función para calcular el peso de la mochila
    def calcula_peso(self):
        return self.peso 

    # Función para verificar si un elemento está en el conjunto
    def verifica_elemento(self, elemento):
        return elemento in self.conjunto

    # Función para calcular el valor de la mochila
    def calcula_valor(self):
        return self.valor 

    # Función para calcular el promedio de alguna de las variables del conjunto de información
    def calcula_promedio(self, numero):
        prom = 0.0
        if(len(Mochila.Informacion) > 0):
            for elemento in Mochila.Informacion:
                prom += Mochila.Informacion[elemento][numero]
            return prom/len(Mochila.Informacion)
        return 0.0

    # Función para generar una copia de la mochila
    def copia(self):
        return Mochila(self.conjunto.copy(), Mochila.Informacion, self.capacidad)
