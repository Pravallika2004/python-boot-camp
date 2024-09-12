s=7
t=11
a=3
b=15
apples=[6,5,-4]
oranges=[9,8,-4]
acount,ocount=0,0
for i in apples:
    if a+i in range(s,t+1):
        acount+=1
for i in oranges:
    if b+i in range(s,t+1):
        ocount+=1
print(acount,ocount)
#hacker rank apple orange sum:one boys house has 2 trees apple and orange here s and t r distance of his house apple tree is distance starts at 3 and orange right to his house distance 15 find how many fruits fall into his house?

