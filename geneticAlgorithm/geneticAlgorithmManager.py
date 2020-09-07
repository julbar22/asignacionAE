from abc import ABC, abstractmethod
from geneticAlgorithm.selectionAlgorithm import SelectionAlgorithm
from geneticAlgorithm.mutationAlgorithm import MutationAlgorithm
from geneticAlgorithm.crossAlgorithm import CrossAlgorithm
from geneticAlgorithm.individual import Individual
import json


class GeneticAlgorithmManager():
    selectionAlgorithm: SelectionAlgorithm = None
    mutationAlgorithm: MutationAlgorithm = None
    crossAlgorithm: CrossAlgorithm = None
    aptitudeThreshold = 0
    finishGenerationBlock = None
    finishRunBlock = None
    individualReference: Individual=None
    enviroment =None

    def __init__(self):
        pass

    def createStartingPopulation(self, populationQuantity: int, individualBase: Individual):
        population = list()
        for i in range(0, populationQuantity):
            population.append(individualBase.createRamdomIndividual(individualBase,self.enviroment))
        return population

    def run(self, populationQuantity: int, generations: int):
        population = self.createStartingPopulation(populationQuantity, self.individualReference)
        for generarionIndex in range(0, generations):
            self.calcularFitnessPopulation(population,self.individualReference)
            print("generation " + str(generarionIndex))
            population=self.selectionAlgorithm.select(population).copy()
            #self.calcularFitnessPopulation(population,self.individualReference)
            population=self.crossAlgorithm.crossPopulation(population,populationQuantity,self.enviroment).copy()
            #self.calcularFitnessPopulation(population,self.individualReference)
            #population=self.mutationAlgorithm.mutationPopulation(population).copy()
            stopGeneration =self.calcularFitnessPopulation(population,self.individualReference)
            self.imprimirPoblacion(population)
            if stopGeneration:
                break
            #json_data = json.dumps(population)
            #print(json_data)

    def imprimirPoblacion(self, poblacion):
        for individuo in poblacion:
            individuo.imprimirIndividuo()
            print(str(individuo.fitness))
    
    def calcularFitnessPopulation(self,poblacion,individualBase):
        terminar =False
        for individuo in poblacion:
            individuo.calculateFitness(individualBase,self.enviroment)
            if individuo.fitness== self.aptitudeThreshold:
                terminar= True
        return terminar

            
