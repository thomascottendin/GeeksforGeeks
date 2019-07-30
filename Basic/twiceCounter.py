#Given an array of n words. Some words are repeated twice, we need count such words.

from collections import Counter

def twiceCounter(string):
    words = string.split()
    wordCount = Counter(words)
    #print(wordCount)
    counter=0
    for x in wordCount:
        key = x
        value = wordCount[key]
        if value==2:
            counter+=1
    return counter


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        numWords=input()
        string=input()
        print(twiceCounter(string))