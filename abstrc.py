from abc import ABC     #absrstact class mean abc
class RBIBank(ABC):
    def interest():
        pass
    def loan():
        print("provides home loan")
class HDFC(RBIBank):
    def interest():
        print("98% interest")
class AXIS(RBIBank):
    def interest():
        print("9% interest")
hobj=HDFC
hobj.interest()
hobj.loan()
robj=RBIBank
robj.loan()
aobj=AXIS
aobj.interest()
aobj.loan()
