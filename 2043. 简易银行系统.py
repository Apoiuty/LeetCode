from typing import List


class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
        self.n = len(self.balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        account1 -= 1
        account2 -= 1
        if account1 < self.n and account2 < self.n and self.balance[account1] - money >= 0:
            self.balance[account1] -= money
            self.balance[account2] += money
            return True
        else:
            return False

    def deposit(self, account: int, money: int) -> bool:
        account -= 1
        if account < self.n:
            self.balance[account] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        account -= 1
        if account < self.n and self.balance[account] >= money:
            self.balance[account] -= money
            return True
        return False
