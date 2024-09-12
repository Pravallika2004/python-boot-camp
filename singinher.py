class JNTU:
    def schedule_acadamic():
        print("scheduled acadamics")
    def declare_holidays():
        print("national and summer holidays")
    def results():
        print('go to www.jnturesults.com')
    # def fees():
    #     print('3rd year fee is 80k')
class SriDevi(JNTU):
    def fees():
        print('3rd year fee is 80k')

sobj=SriDevi
sobj.fees()
sobj.schedule_acadamic()
sobj.declare_holidays()
sobj.results()
jobj=JNTU
jobj.results()
jobj.schedule_acadamic()