#Count the number of 2s as digit in all numbers from 0 to n.

{
#Initial Template for Python 3
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        print(numberOf2sinRange(n))
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
def number0f2s(n):
    count = 0
    arr = map(int, str(n+1))
    for digit in arr:
        if digit == 2:
            count+=1
    return count
    
def numberOf2sinRange(n):
    count=0
    for i in range(n):
        numOf2s = number0f2s(i)
        count+=numOf2s
    return count