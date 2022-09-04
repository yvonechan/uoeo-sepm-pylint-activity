class InsufficientAmount(Exception): 

    pass 

   
class Wallet(object): 

    def __init__(self, initial_amount=0): 
        #Change the initial amount to fail the first test
        self.balance = initial_amount + 1
    
    def spend_cash(self, amount): 
        #Change the InsufficientAmount behaviour
        if self.balance > amount: 

            raise InsufficientAmount('Not enough available to spend {}'.format(amount)) 

        self.balance -= amount 

  

    def add_cash(self, amount): 

        self.balance += amount 