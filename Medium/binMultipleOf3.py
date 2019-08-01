#Given a binary number, write a program that prints 1 if given binary number is a multiple of 3.  Else prints 0.

def isMulitpleOf3(binString):
    num = int(binString, 2)
    if(num%3==0):
        result = 1
    else:
        result = 0
        
    return result
    

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        binString=input()
        print(isMulitpleOf3(binString))