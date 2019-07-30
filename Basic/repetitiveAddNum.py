#Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

def repetitiveAddNum(num):
    
    while(int(num)>9):
        sum=0
        listNum=[]
        for i in range(len(num)):
            listNum.append(num[i])
        for i in listNum:
            sum+=int(i)
        #print(listNum)
        #print(sum)
        num = str(sum)
       
    return num

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        num=input()
        print(repetitiveAddNum(num))