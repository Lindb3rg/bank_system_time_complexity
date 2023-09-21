from datetime import datetime,date,timedelta
from decorators import time_logged_function
import random
from random import randint
from sort_algorithms import quick_sort
        





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
        self._account_prefix = "1111"
        self._account_prefix_boolean = False
        self._balance = 0


    
    def __repr__(self) -> str:
        return self._account_no

    def __str__(self) -> str:
        return self._account_no


    
    def _create_new_name(self):
        list_of_names = ["Börje","Glenn","Kalle Anka", "Rolf","Aragon","Sussie","Bävern"]
        return random.choice(list_of_names)

    
    def _create_new_birthdate(self):
        start = date(1900,1,1)
        end = date.today()
        delta = end - start
        random_days = randint(0,delta.days)
        return start + timedelta(days=random_days)


    def account_prefix(self, prefix:bool):
        
        if prefix == False:
            self._account_prefix_boolean = False
        elif prefix == True:
            self._account_prefix_boolean = True
        


    @property
    def name(self):
        return f"{self._name}"
    

    @property
    def account(self):
        if self._account_prefix_boolean == True:
            return f"{self._account_prefix}-{self._account_no}"
        elif self._account_prefix_boolean == False:
            return self._account_no
        
    
    @account.setter
    def account(self, input):
        self._account_no = input
    




def account_no_formatter(number:int):
    return f"{str(number).zfill(10)}"



@time_logged_function
def create_customers(count:int)->list[Customer]:

    account_list = create_n_accounts(count)
    
    customer_list = []
    for i in range(1,count):
        random_index = random.randrange(len(account_list))
        random_account_no = account_list[random_index]
        account_list[random_index] = account_list[-1]
        account_list.pop()
        customer = Customer(account_no=account_no_formatter(random_account_no))
        customer_list.append(customer)


    return customer_list



@time_logged_function
def load_quick_sort(array):
    quick_sort(array,0, len(array)-1)

@time_logged_function
def create_n_accounts(n_accounts):
    accounts = [i for i in range(n_accounts)]
    return accounts


@time_logged_function
def search_account_no(account_list:list,account_no:str):
    
    if "1111-" in account_no:
        account_no = account_no.replace("1111-","")
    for i in account_list:
        if i.account == account_no:
            i.account_prefix(prefix=True)
            print(f"\n*** Account number found: {i} ***")
            print(f"{i.name}, {i.account}")
            return
        
    return print("Could not find account number")






if __name__=="__main__":
    customer_objects = []
    customer_objects = create_customers(10**5)
    load_quick_sort(customer_objects)
    search_account_no(customer_objects,"1111-0000001000")
    search_account_no(customer_objects,"1111-0009999999")
    search_account_no(customer_objects,"1111-9999999999")
