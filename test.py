import unittest
from app3 import out
class MyTests(unittest.TestCase):

  def test_addition(self):
    result = out()
    self.assertEqual(result,"heyy")
if __name__ == '__main__':
  unittest.main()
