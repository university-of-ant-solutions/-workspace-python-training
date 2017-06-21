import unittest

def f(x):
    f.counter = getattr(f, "counter", 0) + 1 
    return "Monty Python"

class Robot:
  pass

class AMinimalClass_test(unittest.TestCase):

  def test(self):
    ''' define a minimal class '''
    x = Robot()
    y = Robot()
    y2 = y
    self.assertEqual(y == y2, True)
    self.assertEqual(y == x, False)

  def testAttribtest(self):
    ''' test attribtest '''
    x = Robot()
    x.name = "Marvin"
    x.build_year = "1979"
    print(x.__dict__)

    Robot.brand = "Kuka"
    self.assertEqual(x.brand, "Kuka")
    x.brand = "Thales"
    self.assertEqual(Robot.brand, 'Kuka')
    y = Robot()
    self.assertEqual(y.brand, 'Kuka')
    Robot.brand = "Thales"
    self.assertEqual(y.brand, 'Thales')
    self.assertEqual(x.brand, 'Thales')

    # x.energy
    # Traceback (most recent call last):
    #  File "<stdin>", line 1, in 
    #  AttributeError: 'Robot' object has no attribute 'energy'
    self.assertEqual(getattr(x, 'energy', 100), 100)


    for i in range(10):
      f(i)
    self.assertEqual(f.counter, 10)

if __name__ == '__main__':
  unittest.main()
