from datetime import datetime,date,timedelta
from time import time
import random
from random import randint
        
# Jobbar fortfarande på list comprehension
class Customer:
    def __init__(self,account_no, name = None,birthdate=None):
        
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
        self._account_no = {}
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
    


def create_customers(count:int,account_format:int):
    # customer_objects = {str(i).zfill(account_format): Customer() for i in range(1, count)}

    customer_objects = [Customer(account_no = f"account_no-{str(i).zfill(account_format)}") for i in range(1,count)]

    # for i in range(1,count):
    #     customer = Customer()
    #     customer.account = str(i).zfill(account_format)
    #     customer_objects.append(customer)

    
    return customer_objects


def search_account_no(list:list,account_no:str):
    for i in list:
        if i.account == account_no:
            return print(i)
    return print("Could not find account number")





    # 2. Skapa en lista med alla länder som har minst 15 bokstäver i sitt namn. Skriv ut namn och population för varje

    # min_fifthteen_chars = [Country(x["name"],x["capital"],x["currency"],x["population"],x["languages"]) for x in countries if len(x["name"]) >= 15]
    # [print(x) for x in min_fifthteen_chars]

    # 3. Skapa en lista med alla länder som har som börjar på A eller har en huvudstad som börjar på A. Skriv ut namn och capital för varje
    # countries_startswith_A = [Country(x["name"],x["capital"],x["currency"],x["population"],x["languages"]) for x in countries if x["name"].startswith("A") or x["capital"].startswith("A")]

    # [print(f"Country: {x.Name}, Capital: {x.Capital}") for x in countries_startswith_A]



    # 4. Skapa en lista med alla länder som där man pratar English, skriv ut namn och capital för varje 

    # english_speaking_list = [Country(x["name"],x["capital"],x["currency"],x["population"],x["languages"]) for x in countries if "English" in x["languages"]]
    # [print(f"Country: {x.Name}, Capital: {x.Capital}") for x in english_speaking_list]


    # 5. Skapa en lista med FÖRSTA BOKSTAVEN för alla capitals länder som med population mindre än 1000000.  Skriv ut listan i formatet (ex "VAVRST" om det är 6 stycken etc)

    # list_of_country_objects = [Country(x["name"],x["capital"],x["currency"],x["population"],x["languages"]) for x in countries]



    # list_of_country_firstletters = [x.Capital[0] for x in list_of_country_objects if filter_range(x.Population,min=None,max=1000000) and x.Capital != ""]
    



customer_objects = []

if __name__=="__main__":

    # start = time()
    # customer_objects = create_customers(10 ** 7,10)
    # end = time()
    # print(f"10 million customers created in {end-start} seconds.")
    

    # start = time()
    # search_1 = search_account_no(customer_objects,"1111-0000001000")
    # end = time()
    # print(f"Searching for 1111-0000001000 took {end-start} seconds. ")
    

    # start = time()
    # search_2 = search_account_no(customer_objects,"1111-0009999999")
    # end = time()
    # print(f"Searching for 1111-0009999999 took {end-start} seconds. ")
    

    # start = time()
    # search_2 = search_account_no(customer_objects,"1111-9999999999")
    # end = time()
    # print(f"Searching for 1111-9999999999 took {end-start} seconds. ")

    customer_objects = create_customers(10,10)