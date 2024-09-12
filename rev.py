def check(s):
    s=s.split()
    s=list(reversed(s))
    print(s)
    for i in s:
        rev=i[::-1]
        print(rev,end=' ')
s='sri devi'
check(s)


