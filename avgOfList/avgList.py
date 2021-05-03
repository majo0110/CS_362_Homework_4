def calcAvg(arr):
    if (len(arr) != 0):
        totalNum = 0
        for i in range (len(arr)):
            totalNum += arr[i]
        return float(totalNum) / float(len(arr))
    else:
        return 0

if __name__ == '__main__':
    main()
