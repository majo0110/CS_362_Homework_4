import unittest
import avgList

class testCubeVolume(unittest.TestCase):
    def test_RealNum(self):
        tArray1 = [0, 15, 30, 100, 27]
        self.assertEqual(avgList.calcAvg(tArray1), 34.4)

    def test_emptyList(self):
        tArray1 = []
        self.assertEqual(avgList.calcAvg(tArray1), 0)

    def test_zeroList(self):
        tArray1 = [0,0,0,0]
        self.assertEqual(avgList.calcAvg(tArray1), 0)

    def test_string(self):
        tArray1 = ["1", "2", "3", "4"]
        self.assertRaises(avgList.calcAvg(tArray1), "F")

if __name__ == '__main__':
    unittest.main()
