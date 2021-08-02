from abc import ABC, abstractmethod
from frameworkAG.evolutionaryAlgorithm.selectionAlgorithm import SelectionAlgorithm
from frameworkAG.evolutionaryAlgorithm.mutationAlgorithm import MutationAlgorithm
from frameworkAG.evolutionaryAlgorithm.crossAlgorithm import CrossAlgorithm
from frameworkAG.evolutionaryAlgorithm.individual import Individual
from typing import List
import json
import copy
from frameworkAG.evolutionaryAlgorithm.finishAction import FinishAction

class EvolutionaryAlgorithmManager():
    selectionAlgorithm: SelectionAlgorithm = None
    mutationAlgorithm: MutationAlgorithm = None
    crossAlgorithm: CrossAlgorithm = None
    aptitudeThreshold = 0
    finishActions:FinishAction = None
    individualReference: Individual=None
    environment =None
    bestFitness =1000
    bestIndividual:Individual=None

    def __init__(self):
        pass

    def cleanSolution(self):
        self.individualReference = None
        self.environment= None
        self.bestFitness=1000
        self.bestIndividual=None


    def createStartingPopulation(self, populationQuantity: int, individualBase: Individual):
        population = list()
        for i in range(0, populationQuantity):
            population.append(individualBase.createRamdomIndividual(self.environment))
        return population

    def run(self, populationQuantity: int, generations: int):        
        population = self.createStartingPopulation(populationQuantity, self.individualReference)
        for generationIndex in range(0, generations):
            self.calculateFitnessPopulation(population)
            population=self.selectionAlgorithm.select(population).copy()
            if self.bestFitness>population[0].fitness:                
                self.bestFitness= population[0].fitness    
                self.bestIndividual = copy.deepcopy(population[0])   
                #print(population[0].fitness)                 
            population=self.crossAlgorithm.crossPopulation(population,populationQuantity,self.environment).copy()
            population=self.mutationAlgorithm.mutationPopulation(population,self.environment).copy()
            self.calculateFitnessPopulation(population)            
            if self.bestFitness==self.aptitudeThreshold:
                self.bestIndividual.printIndividual()
                print("termino el algoritmo")
                break
            else:
                self.improvementPopulation(population,self.environment)
            self.finishActions.runFinishGenerationBlock(population,self.bestFitness,self.bestIndividual)
        self.finishActions.runFinishRunBlock(population,self.bestFitness,self.bestIndividual)
   
    def calculateFitnessPopulation(self,population):
        for individual in population:
            individual.calculateFitness()
    
    def improvementPopulation(self, population: List[Individual], environment):
        for individual in population:
            individual.improvement(environment)

            
