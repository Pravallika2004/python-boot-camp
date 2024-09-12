# n1=288
# n2=594
# #count the no of carry?
# n1=str(n1)
# n2=str(n2)
# count=0
# j=2
# for i in range(0,len(n1)):
#     if int(n1[j])+int(n2[j])>9:
#         count+=1
#     j-=1    
# print(count)
n1=288
n2=594
carry=0
count=0
while n1>0 and n2>0:
    rem1=n1%10
    rem2=n2%10
    sum=rem1+rem2+carry
    if(sum>9):
        carry=1
        count+=1
    else:
        carry=0
    n1=n1//10
    n2=n2//10
print(count)
