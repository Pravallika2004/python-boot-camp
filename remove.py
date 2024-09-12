s='hello world hello world good mornibg good afternon'
#remove the duplicate words
s=s.split()
n=list(s)
for i in n:
    for j in n:
        if i==j:
            print(n.remove(j))
        
n=str(n)
print(n)
# s=s.split()
# s1=''
# for i in s:
#     if i not in s1:
#         s1=s1+i+' '
# print(s1)


    