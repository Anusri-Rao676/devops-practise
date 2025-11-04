import unittest
from app3 import out
class MyTests(unittest.TestCase):

  def test_addition(self):
    self.assertEqual(out(),'heyy')
if __name__ == '__main__':
  unittest.main()
