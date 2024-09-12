#convert time in 12hr format
time='23:59:60' #o/p:8:
time=time.split(':')
hrs=time[0]
min=time[1]
sncds=time[2]
if int(hrs)>12:
    hrs=int(hrs)-12
if int(sncds)>59:
    min=int(min)+1
    sncds=int(sncds)-60
if int(min)>59:
    hrs=int(hrs)+1
    min=int(min)-60
print(str(hrs)+':'+str(min)+':'+str(sncds))



