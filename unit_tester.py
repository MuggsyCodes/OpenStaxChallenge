# I explored unit testing briefly, one example is below
# I ultimately stayed with VSCode debugger and inline print statements
# in the interest of time
# In terms of efficacy, given how basic this program is, I found it 
# sufficient to test with debugging, inline print statements. 
# Moving forward: I'm planning to learn how to really capitalize on built in 
# unit testing as well some of the python debuggers available like pdb

import unittest

#testing a case-switch statement 

def switcher(self, argument):
  category_switcher = {
      0: 'Pop',
      4: 'Pop',
      8: 'Pop',
      1: 'Science',
      5: 'Science',
      9: 'Science',
      2: 'Sports',
      6: 'Sports',
      10: 'Sports',
  }

  category = category_switcher.get(argument, 'Rock')
  #print(f"Chosen category: {category}")
  return category

class Switcher(unittest.TestCase):
  def check_category(self):
        self.assertEqual(switcher('a'), 'Science')

  def check_bad_input(self):
        self.assertEqual(switcher(12), 'Science')

if __name__ == '__main__':
    unittest.main()

# I was actually in a Google Colab notebook testing this out 
# that's why I had line below
#unittest.main(argv=[''], verbosity=2, exit=False)

