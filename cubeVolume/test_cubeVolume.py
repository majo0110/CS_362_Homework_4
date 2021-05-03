import unittest
import cubeVolume
import cmath

class testCubeVolume(unittest.TestCase):
    def testRegNum(self):
        self.assertEqual(cubeVolume.calcVol(3, 15, 20), 900)

    def test_negNum(self):
        self.assertEqual(cubeVolume.calcVol(-27, 15, 10), -4050)

    def test_string(self):
        self.assertRaises(cubeVolume.calcVol("5", "10", "15"), "F")

    def test_complexNum(self):
        self.assertEqual(cubeVolume.calcVol(complex(10,2), 5, 10), (500 + 100j))

if __name__ == '__main__':
    unittest.main()
