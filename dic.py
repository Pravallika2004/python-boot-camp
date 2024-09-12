menu={
    'chckn_bryn':555,
    'butter_chckn':450,
    'tandoori_chckn':555,
    'juciy_mandi':420,
     }
menu['juicy-mandi']=786
print(menu)
menu.pop('chckn_bryn')
print(menu)
for k,v in menu.items():
     print(k,'->',v)
