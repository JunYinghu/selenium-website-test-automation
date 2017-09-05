from inherritance.animal import Shark
import unittest

class Myclass (unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.shark = Shark('shark')

    def use_shark(self):
        self.shark.swim()
        self.shark.eat()
        self.shark.grow()

    def test_01_callmyclass(self):
        self.use_shark()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Myclass)
    suite.sortTestMethodsUsing = None
    unittest.TextTestRunner(verbosity=2).run(suite)