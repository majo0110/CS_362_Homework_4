import unittest
import avgList

class testCubeVolume(unittest.TestCase):
    def test_RealNum(self):
        tArray1 = [0, 15, 30, 100, 27]
        self.assertEqual(avgList.calcAvg(tArray1), 34.4)

if __name__ == '__main__':
    unittest.main()
