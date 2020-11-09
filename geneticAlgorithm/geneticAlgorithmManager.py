from abc import ABC, abstractmethod
from geneticAlgorithm.selectionAlgorithm import SelectionAlgorithm
from geneticAlgorithm.mutationAlgorithm import MutationAlgorithm
from geneticAlgorithm.crossAlgorithm import CrossAlgorithm
from geneticAlgorithm.individual import Individual
from typing import List
import json
import copy
from geneticAlgorithm.finishAction import FinishAction


class GeneticAlgorithmManager():
    selectionAlgorithm: SelectionAlgorithm = None
    mutationAlgorithm: MutationAlgorithm = None
    crossAlgorithm: CrossAlgorithm = None
    aptitudeThreshold = 0
    finishActions:FinishAction = None
    individualReference: Individual=None
    environment =None
    mejorFitness =1000
    mejorIndividuo:Individual=None

    def __init__(self):
        pass

    def createStartingPopulation(self, populationQuantity: int, individualBase: Individual):
        population = list()
        for i in range(0, populationQuantity):
            population.append(individualBase.createRamdomIndividual(individualBase,self.environment))
        return population

    def run(self, populationQuantity: int, generations: int):        
        population = self.createStartingPopulation(populationQuantity, self.individualReference)
        for generarionIndex in range(0, generations):
            self.calcularFitnessPopulation(population,self.individualReference)
            population=self.selectionAlgorithm.select(population).copy()
            if self.mejorFitness>population[0].fitness:                
                self.mejorFitness= population[0].fitness    
                self.mejorIndividuo = copy.deepcopy(population[0])                    
            population=self.crossAlgorithm.crossPopulation(population,populationQuantity,self.environment).copy()
            population=self.mutationAlgorithm.mutationPopulation(population,self.environment).copy()
            self.calcularFitnessPopulation(population,self.individualReference)            
            if self.mejorFitness==self.aptitudeThreshold:
                print("termino el algoritmo")
                break
            else:
                self.improvementPopulation(population,self.environment)
            self.finishActions.runFinishGenerationBlock(population,self.mejorFitness,self.mejorIndividuo)
        self.finishActions.runFinishRunBlock(population,self.mejorFitness,self.mejorIndividuo)
   
    def calcularFitnessPopulation(self,poblacion,individualBase):
        for individuo in poblacion:
            individuo.calculateFitness(individualBase,self.environment)
    
    def improvementPopulation(self, population: List[Individual], environment):
        for individuo in population:
            individuo.improvement(environment)

            
