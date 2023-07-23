import unittest

class Testcase(unittest.TestCase):
    def setUp(self):
        print("this is  fomr the setup part")

    def testcase(self):
        print('this is from test ')
    
    def tearDown(self):
        print('this is form teardown')


if __name__=="__main__":
    unittest.main()
