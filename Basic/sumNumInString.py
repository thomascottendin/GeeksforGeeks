#Given a string str containing alphanumeric characters, calculate sum of all numbers present in the string.

import re

def sumNumbers(string):
    sum = 0
    listNum = [int(s) for s in re.findall(r'\d+',string)]
    for num in listNum:
        sum+=num
    return sum


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        string=input()
        print(sumNumbers(string))