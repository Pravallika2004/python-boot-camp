s1='tab'
s2='bat'     #seaching for common words in both s1 and s2 called anagram
res1=sorted(s1)  #sorted here helps in making the split of words in list
res2=sorted(s2)
if len(s1)==len(s2) and res1==res2:
    print('anagram')
else:
    print('not anagram')
