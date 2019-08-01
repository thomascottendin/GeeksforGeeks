#Given two numbers as stings s1 and s2 your task is to multiply them. You are required to complete the function multiplyStrings which takes two strings s1 and s2 as its only argument and returns their product as strings.

{
#Initial Template for Python 3
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        a,b=input().split()
        multiply(a,b)
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
def multiply(a,b):
    return print (int(a)*int(b))