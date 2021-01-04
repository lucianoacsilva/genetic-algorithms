from ypstruct import structure
import numpy as np

def run(problem, params):
    
    # Problem information here
    costFunction = problem["costfunc"]
    nvar = problem["nvar"]
    varmin = problem["varmin"]
    varmax = problem["varmax"]
    
    # Parameters
    maxit = params["maxit"]
    npop = params["npop"]   
    
    # Empty Individual Template
    empty_individual = {}
    
    empty_individual["position"] = None
    empty_individual["cost"] = None
    
    # Initialize population
    pop = []
    for i in range(npop):
        pop.append(empty_individual)

    for ind in pop:
        ind["position"] = np.random.uniform(varmin, varmax, nvar)
        ind["cost"] = costFunction(ind["position"])

    out = {}
    out["pop"] = pop

    return out  
    