from random import randint, sample
from itertools import chain, combinations
from time import time
import time
import copy
import random

class SSP():
    def __init__(self, S=[], t=0):
        """ This is the function which initialises the SSP object, which creates the variables required """
        self.S = S              # This is the variable for the set.
        self.t = t              # This is the variable for the target.
        self.n = len(S)         # This is the variable for the length of the set.
        self.decision = False
        self.total    = 0
        self.selected = []

    def __repr__(self):
        """ This is a function used to return a printable representation of the object """
        return "SSP instance: S="+str(self.S)+"\tt="+str(self.t)
    
    def random_instance(self, n, bitlength=10):
        """ This generates a random set of numbers and target. The number of numbers is defined by n, by the user. """
        max_n_bit_number = 2**bitlength-1
        self.S = sorted([ randint(0,max_n_bit_number) for i in range(n) ] , reverse=True)
        self.t = randint(0,n*max_n_bit_number)  # Total is a random int so there might not be a subset that solves the problem.
        self.n = len(self.S)

    def random_yes_instance(self, n, bitlength=10):
        """ This generates a random set of numbers. The number of numbers is defined by n. For the set generated, there will undoubtedly be a subset that equals the total. """
        max_n_bit_number = 2**bitlength-1
        self.S = sorted([ randint(0,max_n_bit_number) for i in range(n) ] , reverse=True)
        self.t = sum(sample(self.S, randint(0,n))) # Total is a sum of a random sample of the set, so there is definetly a subset.
        self.n = len(self.S)

    ###

    def try_at_random(self):
        """ This randomly tries different subsets to see if there is any combination that solves the problem. """
        start = time.clock()
        candidate = []
        total = 0
        while total != self.t:
            candidate = sample(self.S, randint(0,self.n))
            total     = sum(candidate)
            print("(Random) Trying: ", candidate, ", sum:", total)
            if total == self.t:
                print("Success!")
        end = time.clock()
        print (end - start)
            
    def greedy(self): #Fixed previous flaw, but breaks sometimes now. Will solve on Friday.
        """ This takes the largest number smaller than the target and then adds smaller number to attempt to find a soloution. """
        self.S.sort()
        greedlist = self.S
        listchange = 0
        candidate = []
        replace = []
        total = 0
        while total != self.t and greedlist != []:
            if greedlist[-1] > self.t:
                greedlist.pop()
            else:
                listchange = greedlist.pop()
                candidate.append(listchange)
                total = sum(candidate)
                print("(Greedy) Trying: ", candidate, ", sum:", total)
                if total > self.t:
                    candidate.pop()
        if total == self.t:
            print("Success!" , candidate, " adds up to:", self.t)
        else: 
            print("Failure" , candidate, "did not add up to:", self.t)

    def grasp(self): #Fixed previous flaw, but breaks sometimes now. Will solve on Friday.
        """ This takes the largest number smaller than the target and then adds smaller number to attempt to find a soloution. """
        self.S.sort()
        greedlist = self.S
        listchange = 0
        candidate = []
        replace = []
        total = 0
        while total != self.t and greedlist != [] and total < self.t:
            if greedlist[-1] > self.t:
                greedlist.pop()
            else:
                listchange = greedlist.pop()
                candidate.append(listchange)
                total = sum(candidate)
                print("(Greedy) Trying: ", candidate, ", sum:", total)
        counter = 0
        while counter < 5:
            CanIndex = random.randint(0, len(candidate)-1)
            GreedIndex = random.randint(0, len(greedlist)-1)
            replacetotal = (total - candidate[CanIndex]) + greedlist[GreedIndex]
            print (candidate[CanIndex])
            print (greedlist[GreedIndex])
            print (replacetotal)
            if abs(self.t - total) > abs(self.t - replacetotal):
                candidate[CanIndex] = greedlist[GreedIndex]
                print("Replaced: ", candidate)
                total = sum(candidate)
            else:
                print("replacement not more accurate")
            counter+=1
        
        if total == self.t:
            print("Success!" , candidate, " adds up to:", self.t)
        else: 
            print("Failure" , candidate, "did not add up to:", self.t)
            print("It equaled ", total, "this is ", abs(self.t - total), " away.")
            
    def exhaustive(self):
        start = time.clock()
        total = 0
        subsets = [[]]
        next = []
        for j in self.S:
            for i in subsets:
                next.append(i + [j])
            subsets += next
            next =[]
        print (subsets)
        for i in subsets:
            total = sum(i)
            if total == self.t:
                print (i, " is subset of ", self.S, "that equals ", self.t)
                end = time.clock()
                print (end - start)
                break
                
    def dynamic(self):
        values = []
        valuescopy = []
        counter = 0
        start = time.clock()
        for i in self.S:
            #print("i",i)
            if values == []:
                values.append(i)
            else:
                valuescopy = copy.copy(values)
                #print ("length",len(valuescopy))
                while counter < len(valuescopy):
                    #print(len(valuescopy), " ", counter)
                    values.append(valuescopy[counter] + i)
                    if valuescopy[counter] +i == self.t:
                        print ("Target value found using subset of ", self.S)
                        break
                    #print("values",values)
                    counter += 1
                values.append(i)
                counter = 0
        print(values)
        end = time.clock()
        print (end - start)
        
        
instance = SSP()
instance.random_yes_instance(10)
print(instance)

instance.try_at_random()
instance.greedy()
instance.grasp()
instance.exhaustive()
instance.dynamic()
