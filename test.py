import random
import math
from copy import deepcopy

class Terminal:
    def __init__(self, numero, demanda, posx, posy):
        self.numero = numero
        self.demanda = int(demanda)
        self.posx = int(posx)
        self.posy = int(posy)
    
    def getNumero(self):
        return self.numero
    
    def getDemanda(self):
        return self.demanda
    
    def getPosx(self):
        return self.posx

    def getPosy(self):
        return self.posy

    def __str__(self):
        return "{}: {}, ({},{})".format(self.numero, self.demanda, self.posx, self.posy)

class Estacion:
    def __init__(self, numero, capacidad, posx, posy):
        self.numero = numero
        self.capacidad = int(capacidad)
        self.posx = int(posx)
        self.posy = int(posy)
    
    def getNumero(self):
        return self.numero
    
    def getCapacidad(self):
        return self.capacidad
    
    def getPosx(self):
        return self.posx

    def getPosy(self):
        return self.posy

    def __str__(self):
        return "{}: {}, ({},{})".format(self.numero, self.capacidad, self.posx, self.posy)

def calcularDistancia(terminal, estacion):
    return math.sqrt( ((estacion.getPosx() - terminal.getPosx()) ** 2) + ((estacion.getPosy() - terminal.getPosy()) ** 2))

f = [line.split(' ')[:4] for line in open('./Instancias/Ins1.txt').readlines()]

terminalesLst = f[:100]
estacionesLst = f[101:]

terminales = [Terminal(terminal[0], terminal[1], terminal[2], terminal[3]) for terminal in terminalesLst]
estaciones = [Estacion(estacion[0], estacion[1], estacion[2], estacion[3]) for estacion in estacionesLst]

def getDistanciaTotal(d):
    distanciaTotal = 0
    for valor in d.values():
        distanciaTotal += valor[1]
    return distanciaTotal

    

def GRASP(terminales, estaciones):
    resultado = {} # NumeroDeTerminal : NumeroDeEstacion

    # GREEDY

    for terminal in terminales:
        for estacion in estaciones:
            if terminal.getDemanda() <= estacion.getCapacidad():
                estacion.capacidad -= terminal.demanda
                distancia = calcularDistancia(terminal, estacion)
                resultado[terminal.numero] = [estacion.numero, distancia]
                break
    
    # LOCAL SEARCH

    '''
    for terminal in terminales:
        randomSwapIdx = random.randint(len(estaciones))

        randomSwapDist = calcularDistancia(terminal, estaciones[randomSwapIdx])
        distActual = resultado[terminal.getNumero()][0]

        if randomSwapDist < distActual:
    '''

    return resultado


def algoritmo(terminales, estaciones, iteraciones=100):
    distanciasSum = 0
    for _ in range(iteraciones):
        copyTerminales, copyEstaciones = deepcopy(terminales), deepcopy(estaciones)
        random.shuffle(copyTerminales)
        random.shuffle(copyEstaciones)

        resultado = GRASP(copyTerminales, copyEstaciones)
        distanciasSum += getDistanciaTotal(resultado)

    print(distanciasSum/iteraciones)

algoritmo(terminales, estaciones, 1000)


