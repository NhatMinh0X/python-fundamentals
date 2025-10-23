users = {'name':'John', 'age':25, 'phone':'555-1212'}
print(users)

del users['age']
print(users)
'''
pop(key [, default value]): If the key is in the dictionary, it removes the element and
return its value; if not, it returns the default value. If the default value is not provided and
the key is not in the dictionary, the KeyError exception is raised
'''

services = {'FTP': 21, 'SSH': 22, 'SMTP': 25, 'HTTP': 8080, 'LDAP':389, 'HTTPS': 443}
services.pop('HTTPS')
print(services)

'''
popitem(): Removes the last key:value pair from the dictionary and returns it. 
If the dictionary is empty, the KeyError exception is raised.
'''
services.popitem()
print(services)

'''
del d[key]: Deletes the key:value pair. If the key does not exist, the KeyError exception
is thrown.
'''
del services['FTP']
print(services)

'''
clear(): Clears all key:value pairs from the dictionary.
'''
services.clear()
print(services)
