#!/usr/bin/env python
"""Module with two functions, logfactorial(n,k) and choose(n,k), for calculating binomial 
coefficients."""

import math
import argparse

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("-n", type=int, help="number of possibilities")
	parser.add_argument("-k", type=int, help="number of outcomes to choose")
	parser.add_argument("--log", action="store_true", help="whether to return the log of the coefficient instead of the coefficient itself")
	parser.add_argument("--test", action="store_true", help="whether to test the module instead of calculating anything")
	args = parser.parse_args()
	
	# Check that all mandatory arguments are given:
	if not (args.n or args.test):
		raise Exception("Argument n is mandatory.")

def logfactorial(n, k=0):
    """Calculates the log factorial of n (number of possibilities), i.e. 
    log(n!) = log(1) + log(2) + ... + log(n) . n must be a positive integer.
    If a second argument k (number of outcomes) is provided (default: k=0), the function 
    instead calculates log(n!/k!) = log(k+1) + log(k+2) + ... + log(n) . k must also be
    a positive integer.
    Examples:
    >>> round(logfactorial(3), 5)
    1.79176
    >>> round(logfactorial(5,2), 5)
    4.09434
    >>> logfactorial(5,5)
    0
    >>> logfactorial(5,6)
    0
    """
    assert n > 0, "Error: input must be greater than zero."
    assert type(n)==int and type(k)==int, "Error: input must be an integer."
    logfac = 0
    if k > n:
        logfac = 0
    else:
        nlist = list(range(k+1,n+1))
        for step in nlist:
            logfac += math.log(step)
    return logfac

def choose(n,k,log=0):
    """Calculates the binomial coefficient of (n,k), i.e. 'n choose k'. Provide a boolean 
    third argument to specify whether to return the binomial coefficient itself or its log.
    Examples:
    >>> choose(5,1)
    5
    >>> choose(5,2)
    10
    >>> choose(9,5)
    126
    >>> round(choose(5,2,True), 5)
    2.30259
    >>> choose(5,0)
    1
    """
    assert n>0, "Error: n must be greater than zero."
    assert 0 <= k and k <= n, "Error: k must be between zero and n."
    assert type(n) == int and type(k) == int, "Error: n and k must both be integers."
    nmk = n - k
    logcoeff = logfactorial(n,k) - logfactorial(nmk)
    if log:
        return logcoeff
    else:
        return round(pow(2.71828, logcoeff))

def runTests():
    print("Testing the module...")
    import doctest
    doctest.testmod()
    print("Tests complete.")

if __name__ == '__main__' and args.test == True:
    import doctest
    doctest.testmod()
elif __name__ == '__main__':
	print(choose(args.n, args.k, args.log))

