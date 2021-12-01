import random
import math
from copy import deepcopy
import statistics as st

class Terminal:
    def __init__(self, numero, demanda, posx, posy):
        self.numero = int(numero)
        self.demanda = int(demanda)
        self.posx = int(posx)
        self.posy = int(posy)
        self.distancias = {}  # numero de estacion: distancia
    
    def getNumero(self):
        return self.numero
    
    def getDemanda(self):
        return self.demanda
    
    def getPosx(self):
        return self.posx

    def getPosy(self):
        return self.posy

    def __str__(self):
        return "{}: {}, ({},{}), {}".format(self.numero, self.demanda, self.posx, self.posy, self.distancias)

class Estacion:
    def __init__(self, numero, capacidad, posx, posy):
        self.numero = int(numero)
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
    return round(math.sqrt( ((estacion.getPosx() - terminal.getPosx()) ** 2) + ((estacion.getPosy() - terminal.getPosy()) ** 2)))

for fileIdx in range(1,6):
    print('INSTANCIA {}:'.format(fileIdx))

    f = [line.split(' ')[:4] for line in open('./Instancias/Ins{}.txt'.format(fileIdx)).readlines()]

    terminalesLst = f[:100]
    estacionesLst = f[101:]


    def getEstacion(numero, estaciones):
        for estacion in estaciones:
            if estacion.numero == numero:
                return estacion

    def getDistanciaTotal(d):
        distanciaTotal = 0
        for valor in d.values():
            distanciaTotal += valor[1]
        return distanciaTotal

    def getMejorResultado(resultados):
        distancias = [x[1] for x in resultados]
        return min(distancias)

    def getPeorResultado(resultados):
        distancias = [x[1] for x in resultados]
        return max(distancias)

    def getDesviacion(resultados):
        distancias = [x[1] for x in resultados]
        return st.stdev(distancias)

    def GRASP(terminales, estaciones):
        resultado = {} # NumeroDeTerminal : NumeroDeEstacion, distancia

        # GREEDY

        for terminal in terminales:
            i = 0
            while getEstacion(terminal.distancias[i][0], estaciones).getCapacidad() < terminal.getDemanda():
                i += 1
                if i >= len(terminal.distancias): break

            if i >= len(terminal.distancias): i -= 1

            getEstacion(terminal.distancias[i][0], estaciones).capacidad -= terminal.demanda
            distancia = terminal.distancias[i][1]
            resultado[terminal.numero] = [getEstacion(terminal.distancias[i][0], estaciones).numero, distancia]
        
        # LOCAL SEARCH

        return resultado

    def algoritmo(terminales, estaciones, iteraciones=100):
        resultadosFinales = []
        # Calcular la distancia de cada terminal a cada estacion n*m * nlogn
        for terminal in terminales:
            for estacion in estaciones:
                terminal.distancias[estacion.getNumero()] = calcularDistancia(terminal, estacion)
            terminal.distancias = sorted(terminal.distancias.items(), key=lambda x: x[1])
        

        distanciasSum = 0

        for _ in range(iteraciones):
            copyTerminales, copyEstaciones = deepcopy(terminales), deepcopy(estaciones)
            random.shuffle(copyTerminales)
            random.shuffle(copyEstaciones)

            resultado = GRASP(copyTerminales, copyEstaciones)
            distanciaTotal = getDistanciaTotal(resultado)
            distanciasSum += distanciaTotal
            resultadosFinales.append([resultado, distanciaTotal])
            
            '''
            for x,y in resultado.items():
                print(x,y)
            print()
            '''
            

        print('Media:', distanciasSum/iteraciones)
        print('Mejor:', getMejorResultado(resultadosFinales))
        print('Peor:', getPeorResultado(resultadosFinales))
        print('Desviacion:', getDesviacion(resultadosFinales))

    terminalesOriginal = [Terminal(terminal[0], terminal[1], terminal[2], terminal[3]) for terminal in terminalesLst]
    estacionesOriginal = [Estacion(estacion[0], estacion[1], estacion[2], estacion[3]) for estacion in estacionesLst]
    
    algoritmo(terminalesOriginal, estacionesOriginal)


