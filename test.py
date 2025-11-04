import unittest
from app3 import out
class MyTests(unittest.TestCase):
  result = out()
  def test_addition(self):
    self.assertEqual(result,"hello")
if __name__ == '__main__':
  unittest.main()
