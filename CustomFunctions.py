#contains our custom functions

import statistics

def MedianCost(costs):
  """
  Calculates the median cost of a list of costs

  Arguments:
  costs (list)
  """
  medianCost = statistics.median(costs)
  return(f"The median cost per bag is ${medianCost}")

def MinCost(costs):
  """
  Calculates the min cost from a list of costs

  Arguments:
  costs (list)
  """
  minCost = min(costs)
  return(f"The minimum cost per bag is ${minCost}")

def MaxCost(costs):
  """
  Calculates the max cost from a list of costs

  Arguments:
  costs (list)
  """
  maxCost = max(costs)
  return(f"The maximum cost per bag is ${maxCost}")

def MostExpensive(costs, names):
  """
  Finds the name of the most expensive item

  Arguments:
  costs (list), names (list)
  """
  mostExpensive = names[costs.index(max(costs))]
  return(f"The most expensive bag is {mostExpensive}")

def MostExpensivePerGram(costs, names, weights):
  """
  Finds the name of the most expensive item per gram

  Arguments:
  costs (list), names (list), weights (list)
  """
  #pricePerHundred
  pPH = []
  for i in range(len(names)):
    pPH.append((weights[i]/costs[i])*100)
  mostExpensivePerGram = names[pPH.index(max(pPH))]
  return(f"The most expensive bag per gram is {mostExpensivePerGram}
