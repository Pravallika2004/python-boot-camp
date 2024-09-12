def check(n):
    sum=1
    first=0
    
    second=1
    print(first,second,end=' ')
    count=2
    while count<=n:
        third=first+second
        print(third,end=' ')
        sum=sum+third
        first=second
        second=third
        count+=1
    return sum
print(check(7),end='')

# check(7)
