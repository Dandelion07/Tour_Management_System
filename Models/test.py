from DatabaseManager import DatabaseManager
from Account import Account, AccessLevel

res = Account.SignIn('user', 'user', 2)
print(res)
