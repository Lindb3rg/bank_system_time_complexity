from datetime import datetime,date,timedelta
from decorators import time_logged_function
import random

        





class Customer:


    def __init__(self,account_no:int, name = None,birthdate=None):
        
        
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
        self._account_no = account_no
        self._balance = 0


    
    def __repr__(self) -> str:
        return f"{self._name}"


    def _create_new_name(self):
        list_of_names = ["Börje","Glenn","Kalle Anka", "Rolf","Aragon","Sussie","Bävern"]
        return random.choice(list_of_names)


    def _create_new_birthdate(self):
        start = date(1900,1,1)
        end = date.today()
        delta = end - start
        random_days = random.randint(0,delta.days)
        return start + timedelta(days=random_days)



    @property
    def account(self):
        return self._account_no

    


def account_no_formatter(number:int, account_prefix="1111"):
    return f"{account_prefix}-{str(number).zfill(10)}"



@time_logged_function
def create_customers(count:int):

    customer_dicts = {}

    [customer_dicts.update({account_no_formatter(i): Customer(account_no=account_no_formatter(i))}) for i in range(1,count)]

    return customer_dicts


@time_logged_function
def search_account_no(customer_dict:dict,account_no:str):

    if account_no in customer_dict:

        return print(customer_dict[account_no])

    else:

        return print(f"Could not find {account_no} in incoming dict") 
    




if __name__=="__main__":
    
    customer_objects = create_customers(10 ** 7)
    
    search_1 = search_account_no(customer_objects,"1111-0000001000")
    
    search_2 = search_account_no(customer_objects,"1111-0009999999")
    
    search_3 = search_account_no(customer_objects,"1111-9999999999")
    

