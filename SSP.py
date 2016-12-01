from random import randint, sample
from itertools import chain, combinations
from time import time

class SSP():
    def __init__(self, S=[], t=0):
    """ This is the function which initialises the SSP object, which
        creates the variables required """
        self.S = S              # This is the variable for the set.
        self.t = t              # This is the variable for the target.
        self.n = len(S)         # This is the variable for the length of the set.
        #
        self.decision = False
        self.total    = 0
        self.selected = []

    def __repr__(self):
    """ This is a function used to return a printable representation of the object """
        return "SSP instance: S="+str(self.S)+"\tt="+str(self.t)
    
    def random_instance(self, n, bitlength=10):
        max_n_bit_number = 2**bitlength-1
        self.S = sorted( [ randint(0,max_n_bit_number) for i in range(n) ] , reverse=True)
        self.t = randint(0,n*max_n_bit_number)
        self.n = len( self.S )

    def random_yes_instance(self, n, bitlength=10):
        max_n_bit_number = 2**bitlength-1
        self.S = sorted( [ randint(0,max_n_bit_number) for i in range(n) ] , reverse=True)
        self.t = sum( sample(self.S, randint(0,n)) )
        self.n = len( self.S )

    ###

    def try_at_random(self):
        candidate = []
        total = 0
        while total != self.t:
            candidate = sample(self.S, randint(0,self.n))
            total     = sum(candidate)
            print( "Trying: ", candidate, ", sum:", total )
            
    def greedy(self):
        self.S.sort()
        greedlist = self.S
        listchange = 0
        candidate = []
        total = 0
        while total < self.t:
            if greedlist[-1] > self.t:
                greedlist.pop()
            else:
                listchange = greedlist.pop()
                candidate.append(listchange)
                total = sum(candidate)
                print( "Trying: ", candidate, ", sum:", total )
        if total == self.t:
            print( candidate, " adds up to:", total )
        else:
            print( candidate, " did not add up to:", total)
    
instance = SSP()
instance.random_yes_instance(4)
print( instance )

instance.try_at_random()
