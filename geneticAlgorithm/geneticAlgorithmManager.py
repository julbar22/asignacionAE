from abc import ABC, abstractmethod
from geneticAlgorithm.selectionAlgorithm import SelectionAlgorithm
from geneticAlgorithm.mutationAlgorithm import MutationAlgorithm
from geneticAlgorithm.crossAlgorithm import CrossAlgorithm
from geneticAlgorithm.individual import Individual
from typing import List
import json


class GeneticAlgorithmManager():
    selectionAlgorithm: SelectionAlgorithm = None
    mutationAlgorithm: MutationAlgorithm = None
    crossAlgorithm: CrossAlgorithm = None
    aptitudeThreshold = 0
    finishGenerationBlock = None
    finishRunBlock = None
    individualReference: Individual=None
    environment =None

    def __init__(self):
        pass

    def createStartingPopulation(self, populationQuantity: int, individualBase: Individual):
        population = list()
        for i in range(0, populationQuantity):
            population.append(individualBase.createRamdomIndividual(individualBase,self.environment))
        return population

    def run(self, populationQuantity: int, generations: int):
        mejor = 1000
        mejorIndividuo =None
        
        population = self.createStartingPopulation(populationQuantity, self.individualReference)
        for generarionIndex in range(0, generations):
            self.calcularFitnessPopulation(population,self.individualReference)
            #print("generation " + str(generarionIndex))
            population=self.selectionAlgorithm.select(population).copy()
            if mejor>population[0].fitness:                
                mejor= population[0].fitness    
                mejorIndividuo = population[0].errores.copy()        
                population[0].imprimirIndividuo()
                print(population[0].fitness)
                print("generacion:"+str(generarionIndex))
                population[0].imprimirErrores()
            
            population=self.crossAlgorithm.crossPopulation(population,populationQuantity,self.environment).copy()
            population=self.mutationAlgorithm.mutationPopulation(population,self.environment).copy()
            self.calcularFitnessPopulation(population,self.individualReference)
            
            if mejor==self.aptitudeThreshold:
                print(str(generarionIndex))
                break
            else:
                self.improvementPopulation(population,self.environment)
        print(len(mejorIndividuo))

    def imprimirPoblacion(self, poblacion):
        for individuo in poblacion:
            #individuo.imprimirIndividuo()
            print(str(individuo.fitness))
    
    def calcularFitnessPopulation(self,poblacion,individualBase):
        for individuo in poblacion:
            individuo.calculateFitness(individualBase,self.environment)
    
    def improvementPopulation(self, population: List[Individual], environment):
        for individuo in population:
            individuo.improvement(environment)

            
