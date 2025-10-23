def contains(dictionaries:dict, item):
    for key, value in dictionaries.items():
        if item == value:
            return True
    return False

dictionary = {1:100, 2:200, 3:300}
print(contains(dictionary, 200))
print(contains(dictionary, 300))
print(contains(dictionary, 350))