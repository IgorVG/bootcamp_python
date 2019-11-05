#!/usr/bin/env python3

import warnings


class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1
    
    def transfer(self, amount):
        self.value += amount

class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = []

    def corrupted(self, account):
        return not len(dir(account) % 2 ) or not all(not x.startswith('b') and not x.startswith('zip') and not x.startswith('addr') for x in dir(account)) or not 'name' in dir(account) or not 'id' in dir(account) or not 'value' in dir(account)
    
    def check_security(self, origin, dest, amount):
        if not isinstance(origin, Account) or not isinstance(dest, Account) or origin.amount < amount:
            return True

    def add(self, account):
        self.accounts.append(account)

    def transfer(self, origin, dest, amount):
        """
            @origin:  int(id) or str(name) of the first account
            @dest:    int(id) or str(name) of the destination account
            @amount:  float(amount) amount to transfer
            @return         True if success, False if an error occured
        """
        if self.check_security(origin, dest, amount):
            warnings.warn('Error of security check')
            return False
        if self.corrupted(origin):
            if self.fix_account(origin):
                pass
            else:
                warnings.warn('Cannot fix corrupted origin')
                return False
        if self.corrupted(dest):
            if self.fix_account(dest):
                pass
            else:
                warnings.warn('Cannot fix corrupted dest')
                return False
        origin.value -= amount
        dest.value += amount
        return True
        
        #check_corrupted(origin)
        #check_corrupted(dest)

    def fix_account(self, account):
        """
            fix the corrupted account
            @account: int(id) or str(name) of the account
            @return         True if success, False if an error occured
        """
        if not 'name' in dir(account):
            account.__dict__['name'] = 'default'
        if not 'id' in dir(account):
            account.__dict__['id'] = Account.ID_COUNT
            Account.ID_COUNT += 1
        if not 'value' in dir(account):
            account.__dict__['value'] = 0
        for x in dir(account):
            if x.startswith('b'):
                account.__dict__.pop(x)
            elif x.startwith('zip'):
                account.__dict__.pop(x)
            elif x.startwith('addr'):
                account.__dict__.pop(x)
        if not len(dir(accont)) % 2:
            return False
        else:
            return True

if __name__ == '__main__':
    a1 = Account()
    a2 = Account()