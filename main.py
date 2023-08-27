# Du ska ha en LISTA med OBJEKT (kund-klass)
# Varje kund ska ha:
# created (timestamp)
# last updated (timestamp)
# name
# birthdate (date)
# kontonummer (1234-1234567890) formatvalidering (4 siffror sedan - sedan 10 siffror) saldo

from datetime import datetime
import names

class Customer:
    def __init__(self, name:str,birthdate):
        
        if self.name == None:
            self.name = self._create_new_name()
        else:
            self.name = name

        if self.birthdate == None:
            self.birthdate = self._create_new_birthdate()
        else:
            self.birthdate = birthdate

        self.created = datetime.datetime.now()
        self.last_updated = datetime.datetime.now()
        self.account_no = self._create_new_account()
        self.balance = 0


    def _create_new_name(self):
        self.name = names.get_first_name()

    def _create_new_birthdate(self):
        pass
    
    def _create_new_account(self):
        pass


        
