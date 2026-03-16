import unittest;

from mymodule2 import add

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3),5)
        self.assertEqual(add(-1,1),0)
        self.assertEqual(add(0,0),0)
        self.assertEqual(add("hello","world"),'helloworld')
        
        
unittest.main()        
        

