#Given an sorted array A[i] of N positive integers having all the numbers occuring exactly twice, except for one number which will occur only once. Find the number occuring only once.

from collections import Counter

def appearOnce(strNum):
    arr = strNum.split()
    numCount = Counter(arr)
    #print(numCount)
    for x in numCount:
        key = x
        value = numCount[key]
        if value==1:
            return key


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a=input()
        strNum=input()
        print(appearOnce(strNum))