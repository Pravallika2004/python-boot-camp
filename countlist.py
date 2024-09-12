trs={
    7:54,
    25:60,
    30:45,
    17:55,
    40:67,}
tdp={
    7:54,
    25:60,
    30:45,
    17:55,
    40:67,}
maxtrs=0
for age,votes in trs.items():
    if age>=18:
        maxtrs+=votes
maxtdp=0
for age,votes in tdp.items():
    if age>=18:
        maxtdp+=votes
if (maxtrs>maxtdp):
    
    print('trs has max votes',maxtrs)
else:
    print('tdp has max votes',maxtdp)
     