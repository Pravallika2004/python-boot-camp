s='abcdz'
# s1=''
# for c in s:
#     if ord(c)>=97 and ord(c)<122:
#         print(chr(ord(c)+1))
#         s1+=chr(ord(c)+1)
#     else:
#         s1+=chr(ord(c)-25)
# print(s1)
str=' '
for i in s:
    if i=='z':
        str+='a'
    else:
        str+=chr(ord(i)+1)
print(str)