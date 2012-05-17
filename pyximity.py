from numpy import *

class Pyximity:
  
  def __init__(self, neighbors, values):
    self.neighbors = neighbors
    self.values = values
    
  def regress(self, target, k=5, kernel=lambda dNorm: 1 - dNorm):
    return Pyximity.regressWith(target, self.neighbors, self.values, k, kernel)
    
  @staticmethod
  def regressWith(target, neighbors, values, k=5, kernel=lambda dNorm: 1 - dNorm):
    neighborCount = neighbors.shape[0]

    #Using Euclidian distance
    distances = ((tile(target, (neighborCount, 1)) - neighbors)**2).sum(axis=1)**0.5
    sortedDistanceIndexes = distances.argsort()[0:k]
    maxDistance = double(distances[sortedDistanceIndexes[-1]])

    weights = array([double(kernel(distances[i] / maxDistance)) for i in sortedDistanceIndexes])
    weightSum = sum(weights)
    weightsNorm = weights / weightSum

    return sum(array([values[i] for i in sortedDistanceIndexes]) * weightsNorm)