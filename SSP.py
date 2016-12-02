from random import randint, sample
from itertools import chain, combinations
from time import time
import time

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
        total = 0
        while total != self.t:
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
                
def subsetsum( array , num):
    if num == 0 or num < 1:
        print("a")
    elif len(array) == 0:
        print("b")
    else:
        if array[0] == num:
            print(array)
            return [array[0]]
        else:
            with_v = subsetsum(array[1:],(num - array[0])) 
            if with_v:
                print(array)
                return [array[0]] + with_v
            else:
                print("c")
                return subsetsum(array[1:],num)
subset = [100, 50, 300, 400]
lengt = 700
subsetsum(subset, lengt)

instance = SSP()
instance.random_yes_instance(4)
print(instance)

instance.try_at_random()
instance.greedy()
instance.exhaustive()
