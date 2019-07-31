#Given an unsorted array of size N of positive integers. One number 'A' from set {1, 2, …N} is missing and one number 'B' occurs twice in array. Find these two numbers.


from collections import Counter

def findMissingRepeating(listNum):
    
    numCount = Counter(listNum)

    repList=[]
    for x in numCount:
        key = x
        value = numCount[key]
        if value==2:
            repList.append(key)
    repNum = str(repList[0])
    
    missList=[]
    for i in range(len(listNum)):
        if i+1 not in listNum:
            missList.append(i+1)
    missNum = str(missList[0])
    
    return repNum + ' ' + missNum

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a=input()
        
        str_arr = input().split() #will take in a string of numbers separated by a space
        arr = [int(num) for num in str_arr] #//!\\ Memory Error if array is too long :(
        arr.sort()
        print(findMissingRepeating(arr))