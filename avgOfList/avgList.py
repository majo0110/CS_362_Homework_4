def calcAvg(arr):
    totalNum = 0
    for i in range (len(arr)):
        totalNum += arr[i]
    return float(totalNum) / float(len(arr))

def main():
    testArr = [0,1,2,3,4]
    print(calcAvg(testArr))

if __name__ == '__main__':
    main()
