def calcAvg(arr):
    totalNum = 0
    for i in range (len(arr)):
        totalNum += arr[i]
    return float(totalNum) / float(len(arr))

if __name__ == '__main__':
    main()
