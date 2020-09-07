from geneticAlgorithm.individual import Individual
from typing import List
import random
import string

class Word(Individual):

    def __init__(self):
        pass

    def calculateFitness(self, individual: Individual):
        self.fitness=0
        for index in range(0,len(individual.cromosoma)):
            if individual.cromosoma[index]!=self.cromosoma[index]:
                self.fitness+=1

    def createRamdomIndividual(self,individualBase: Individual,environment)->Individual:
        cromosomaString= "".join(random.choice(string.ascii_letters) for _ in range(len(individualBase.cromosoma)))
        nuevo = Word()
        nuevo.cromosoma =list(cromosomaString)
        return nuevo

    def mutate(self, index:int):
        cromosomaString= "".join(self.cromosoma[0:index]) + random.choice(
        string.ascii_letters) + "".join(self.cromosoma[index+1:len(self.cromosoma)])
        self.cromosoma = list(cromosomaString)
        return self

 