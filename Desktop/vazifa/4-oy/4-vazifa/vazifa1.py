from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __new__(cls, *args, **kwargs):
        if cls is BankAccount:
            raise TypeError("BankAccount obyektini to'g'ridan-to'g'ri yaratib bo'lmaydi")
        return super().__new__(cls)

    def __init__(self, account_number, owner, balance=0):
        self._account_number = account_number
        self._owner = owner
        self._balance = max(balance, 0)

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Summa musbat bo'lishi kerak")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Summa musbat bo'lishi kerak")
        if amount > self._balance:
            raise ValueError("Balansda yetarli pul yo'q")
        self._balance -= amount

    @abstractmethod
    def get_info(self):
        pass

    def __str__(self):
        return f"{self._owner} ({self._account_number}) | Balance: {self._balance}"

    def __repr__(self):
        return f"{type(self).__name__}({self._account_number!r}, {self._owner!r}, {self._balance!r})"

    def __bool__(self):
        return self._balance > 0

    def __eq__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented
        return self._account_number == other._account_number

    def __ne__(self, other):
        natija = self.__eq__(other)
        return natija if natija is NotImplemented else not natija

    def __hash__(self):
        return hash(self._account_number)

    def __gt__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented
        return self._balance > other._balance

    def __ge__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented
        return self._balance >= other._balance

    def __lt__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented
        return self._balance < other._balance

    def __le__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented
        return self._balance <= other._balance


class SavingsAccount(BankAccount):
    def __init__(self, account_number, owner, balance=0, foiz=5):
        super().__init__(account_number, owner, balance)
        self.foiz = foiz

    def get_info(self):
        return f"Savings Account: {self._owner}, Balance: {self._balance}, Foiz: {self.foiz}%"


class BusinessAccount(BankAccount):
    def __init__(self, account_number, owner, balance=0, kompaniya="N/A"):
        super().__init__(account_number, owner, balance)
        self.kompaniya = kompaniya

    def get_info(self):
        return f"Business Account: {self._owner}, Kompaniya: {self.kompaniya}, Balance: {self._balance}"


account1 = SavingsAccount(1, "Mubina", 2000, 7)
account2 = BusinessAccount(2, "Munisa", 2100, "TechUz")

print(account1)
print(repr(account1))
print(bool(account1))
print(account1 == account2)
print(account1 != account2)
print(account1 > account2)
print(account1 <= account2)

print(account1.get_info())
print(account2.get_info())

try:
    BankAccount(3, "Test")
except TypeError as xato:
    print(xato)

    