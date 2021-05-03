import unittest
import genName

class testCubeVolume(unittest.TestCase):
    def test_RegName(self):
        self.assertEqual(genName.genFullName("bobby", "lee"), "bobby lee")

    def test_threeNames(self):
        self.assertEqual(genName.genFullName("Mcdonald Middle name", "jenkins"), "Mcdonald Middle name jenkins")

    def test_integers(self):
        self.assertEqual(genName.genFullName(200, 3004), 3204)


if __name__ == '__main__':
    unittest.main()
