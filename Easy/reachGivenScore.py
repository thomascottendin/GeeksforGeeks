#Consider a game where a player can score 3 or 5 or 10 points in a move. Given a total score n, find number of distinct combinations to reach the given score.
#Variation of Coin Change
#Source code: https://www.geeksforgeeks.org/coin-change-dp-7/

def count(S, m, n): 
    table = [0 for k in range(n+1)] 
    table[0] = 1
    for i in range(0,m): 
        for j in range(S[i],n+1): 
            table[j] += table[j-S[i]] 
  
    return table[n] 

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        score=int(input())
        print(count([3,5,10], 3, score))