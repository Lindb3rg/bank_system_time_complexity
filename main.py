# Du ska ha en LISTA med OBJEKT (kund-klass)
# Varje kund ska ha:
# created (timestamp)
# last updated (timestamp)
# name
# birthdate (date)
# kontonummer (1234-1234567890) formatvalidering (4 siffror sedan - sedan 10 siffror) saldo

from datetime import datetime


class Customer:
    def __init__(self, name:str,birthdate):
        self.name = name
        self.birthdate = birthdate
        self.created = datetime.datetime.now()
        self.last_updated = datetime.datetime.now()
        self.account_no = self._assign_new_account()
    



    def _assign_new_account(self):
        pass
        
