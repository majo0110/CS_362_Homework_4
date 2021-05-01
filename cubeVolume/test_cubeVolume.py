import unittest
import cubeVolume

class testCubeVolume(unittest.TestCase):
    def testRegNum(self):
        self.assertEqual(cubeVolume.calcVol(3, 15, 20), 900)

if __name__ == '__main__':
    unittest.main()
