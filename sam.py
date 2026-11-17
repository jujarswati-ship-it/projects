from abc import ABC,abstractmethod
class payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class upi(payment):
    def pay(self,amount):
        print("paid using upi",amount)

class card(payment):
    def pay(self,amount):
        print("paid using card",amount)

u=upi()
u.pay(500)

