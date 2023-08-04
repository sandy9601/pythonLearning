class SavingAccount:
    def __init__(self,amount) -> None:
        self._amount=amount
    def get_amount(self):
        print("current balance ===>",self._amount)





user=SavingAccount(10000)

user.get_amount()

print(user._amount)