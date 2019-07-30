if __name__ == '__main__':
    for _ in range(int(input())):
        string = input()
        reverseString=''
        i = len(string)-1
        while i>=0:
            reverseString+=string[i]
            i-=1
        print(reverseString)