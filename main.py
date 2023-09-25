from datetime import datetime,date,timedelta
import random
from random import randint
from decorators import time_logged_function



class Customer:
    def __init__(self,name = None,birthdate=None):
        
        if name is None:
            self._name = self._create_new_name()
        else:
            self._name = name
        if birthdate is None:
            self._birthdate = self._create_new_birthdate()
        else:
            self._birthdate = birthdate
        self._created = datetime.now()
        self._last_updated = datetime.now()
        self._account_no = None
        self._account_prefix = "1111-"
        self._balance = 0
    
    def __repr__(self) -> str:
        return f"{self._account_no}"

    def _create_new_name(self):
        list_of_names = ["Börje","Glenn","Kalle Anka", "Rolf","Aragon","Sussie","Bävern"]
        return random.choice(list_of_names)

    def _create_new_birthdate(self):
        start = date(1900,1,1)
        end = date.today()
        delta = end - start
        random_days = randint(0,delta.days)
        return start + timedelta(days=random_days)



    @property
    def account(self):
        return self._account_no
    
    @account.setter
    def account(self, input):
        self._account_no = self._account_prefix + input
    

@time_logged_function
def create_customers(count:int,account_format:int):
    customer_objects = []
    for i in range(1,count):
        customer = Customer()
        customer.account = str(i).zfill(account_format)
        customer_objects.append(customer)

    
    return customer_objects

@time_logged_function
def search_account_no(list:list,account_no:str):
    for i in list:
        if i.account == account_no:
            return print(i)
    return print("Could not find account number")





customer_objects = []

if __name__=="__main__":

    
    customer_objects = create_customers(10 ** 7,10)
    
    search_1 = search_account_no(customer_objects,"1111-0000001000")    

    search_2 = search_account_no(customer_objects,"1111-0009999999")

    search_3 = search_account_no(customer_objects,"1111-9999999999")
    
    