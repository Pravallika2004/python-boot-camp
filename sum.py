# n1=7823
# n2=5489
# n3=1384
# # find sum of all min digits sum of all max digit and find difference
# def check(n):             
#     s=str(n)
#     min=int(s[0])
#     max=int(s[0])
#     for i in s:
#         if int(i)<min:
#             min=int(i)
#         if int(i)>max:
#             max=int(i)
#     print(min,max)
#     return(abs(max-min))     #abs return only the posititve one   
#      #l=[n1,n2,n3]  
#      #                                
# val1=check(n1)
# val2=check(n2)
# val3=check(n3)
# print(val1+val2+val3)

max_sum=0
min_sum=0
def min_check(n):
    s=str(n)
    min=int(s[0])
    for i in s:
        if int(i)<min:
            min=int(i)
    return min
def max_check(n):
    s=str(n)
    max=int(s[0])
    for i in s:
        if int(i)<max:
            max=int(i)
    return max
n1=7823
n2=5489
n3=1384
min_sum=min_check(n1)+min_check(n2)+min_check(n3)
max_sum=max_check(n1)+max_check(n2)+max_check(n3)
diff=abs(min_sum-max_sum)