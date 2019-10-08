import unittest
import unittest1

class TestUnittest1(unittest.TestCase):

    def setUp(self):
        print('setUp')
        self.add = unittest1.add(10, 5) # Просто для примера, лучше использовать для инициализации классов

    def tearDown(self):
        print('tearDown\n')

    def test_add(self):
        #result = unittest1.add(10, 5)
        #self.assertEqual(result, 15)
        self.assertEqual(self.add, 15)
        self.assertEqual(unittest1.add(-1, 1), 0)
        self.assertEqual(unittest1.add(-1, -1), -2)

    def test_divide(self):
        self.assertEqual(unittest1.divide(10, 5), 2)
        self.assertEqual(unittest1.divide(-1, 1), -1)
        self.assertEqual(unittest1.divide(-1, -1), 1)
        self.assertEqual(unittest1.divide(5, 2), 2.5)

        #self.assertRaises(ValueError, unittest1.divide, 10, 0)
        with self.assertRaises(ValueError):
            unittest1.divide(10, 0)

#unittest.main()
if __name__ == '__main__':
    unittest.main()