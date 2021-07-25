def larg_Word(s):

    s = sorted(s, key=len)
    print(s)
    print("largest word:", s[-1])
    print("smallest word:",s[0])

    #print(s[-3] + "$" + s[6])

if __name__ == "__main__":
    s = "Hi i am atul Kumarw Patel"
    print(s)
    arr  = s.split(" ");
    print(arr)
    #for i in range(0, len(s)):
       #print (arr[i])

    l = list(arr)
    print(l)
    larg_Word(l)
