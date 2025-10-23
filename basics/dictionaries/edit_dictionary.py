users = {'name':'John', 'age':25, 'phone':'555-1212'}
print(users)
users['age'] = 30
print(users)

users2 = {'name':'Mari', 'age':27, 'phone':'555-1214'}
users.update(users2)
print(users)