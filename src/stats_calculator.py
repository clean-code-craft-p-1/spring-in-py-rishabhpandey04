import math

def calculateStats(numbers):
  # implement the computation of statistics here and return the results
  
  if len(numbers) > 0:
    return {
      "avg": sum(numbers) / len(numbers),
      "max": max(numbers),
      "min": min(numbers)
    }
  elif len(numbers) == 0:
    return {
      "avg": math.nan,
      "max": math.nan,
      "min": math.nan
    }

  return None