motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
#  Popping Items from Any Position in a List
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a '{first_owned.title()}'.")