def larg_Word(s):

    s = sorted(s, key=len)

    print(s[-1])
if __name__ == "__main__":
    s = "Hi i am atul Kumar Patel "

    l = list(s.split(" "))
    larg_Word(l)
