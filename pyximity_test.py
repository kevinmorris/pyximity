from numpy import *
import unittest
from pyximity import *

class PyximityTest(unittest.TestCase):
  
  def testRegression(self):
    
    coordinates = array([[1., 5.], [1.1, 1.], [3., 3.], [3.8, 6.7], [6., 2.2], [6.4, 0.8], [8., 4.8], [8.6, 3.]])
    values = array([48., 64., 57., 72., 50., 52., 68., 61.])
    p = Pyximity(coordinates, values)
    
    target = array([5.7, 4])
    self.assertEqual(56.973101225284019, p.regress(target))
    
  def testClassRegression(self):
    
    coordinates = array([[1., 5.], [1.1, 1.], [3., 3.], [3.8, 6.7], [6., 2.2], [6.4, 0.8], [8., 4.8], [8.6, 3.]])
    values = array([48., 64., 57., 72., 50., 52., 68., 61.])
    
    target = array([5.7, 4])
    self.assertEqual(56.973101225284019, Pyximity.regressWith(target, coordinates, values))
    

if __name__ == '__main__':
    unittest.main()    