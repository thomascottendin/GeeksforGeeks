#Given a number N. The task is to complete the function convertFive() which replace all zeros in the number with 5 and returns the number.

{
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n=int(input())
        print(convertFive(n))
# Contributed by: Harshit sidhwa

}
''' This is a function problem.You only need to complete the function given below '''
#function should return an integer
#3your task is to compplete this function
def convertFive(n):
    #Code here
    return str(n).replace("0", "5")