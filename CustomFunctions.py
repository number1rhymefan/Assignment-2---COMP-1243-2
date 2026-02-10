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

#2nd Change
#contains our custom functions
bags_size = []
bags_cost = []
product_names = []
highest_expensiveitem_pergram = []
most_expensiveitme_pergram = []
go = True
while (go):
  ans = input("Do you want to input data? (say 'yes' to contuine and 'done' to stop):")
  if ans == "yes":
    bag_size = float(input("What is the size of the bag of vegitable purchased in grams?"))
    bags_size.append(bag_size)
    bag_cost = float(input("What is the cost of the bag of vegitable purchesd"))
    bags_cost.append(bag_cost)
    product_name = float(input("What is the name of the product?"))
    product_names.append(product_name)
    cost_per_100g = (bag_cost/ bag_size)*100
    print(f"{product_name}  costs per 100g is ${cost_per_100g:.3f}/100 grams")
    go = True
  elif ans == "done":
    go = False
  else:
    print("Please write the correct ans")

if len(bags_cost)>0:
  overall_cost = sum(bags_cost)
  print(overall_cost)
  overall_cost_per_100g = (overall_cost/ overall_weight)*100
  print(overall_cost_per_100g)
  mean_cost_perbag = (overall_cost)/len(bags_cost)
  print(mean_cost_perbag)
else:
  print("havent entered anything")
