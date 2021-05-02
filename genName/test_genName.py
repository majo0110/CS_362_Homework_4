import unittest
import genName

class testCubeVolume(unittest.TestCase):
    def test_RegName(self):
        self.assertEqual(genName.genFullName("bobby", "lee"), "bobby lee")

if __name__ == '__main__':
    unittest.main()
