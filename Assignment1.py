bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)    #['trek', 'cannondale', 'redline', 'specialized']

# List indexing
print(bicycles[0])
print(bicycles[1])

# string method
print(bicycles[0].title())
print(bicycles[1].title())  # Output: trek, cannondale, Trek, Cannondale

# message typing with single element of list
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)  #Output : My first bicycle was a Trek.

# my example
uma_mah = f'My father bought {bicycles[2].title()} for me, but I am bad at cycling.'
print(uma_mah)    #Output: My father bought Redline for me, but I am bad at cycling.

# list modification
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
#Output ['honda', 'yamaha', 'suzuki']

motorcycles[0] = 'ducati'
print(motorcycles)
# Output ['ducati', 'yamaha', 'suzuki']

# Append() for empty list
motorcycles2 = []
motorcycles2.append('honda')
motorcycles2.append('yamaha')
motorcycles2.append('suzuki')
print(motorcycles2)
print(f'Motorcycles available in showroom are: {motorcycles2}')
#Output: ['honda', 'yamaha', 'suzuki']
Motorcycles available in showroom are: ['honda', 'yamaha', 'suzuki']

# insert()
motorcycles3 = ['honda', 'yamaha', 'suzuki']
motorcycles3.insert(0, 'ducati')
motorcycles3.insert(3, 'flash')
print(motorcycles3)
#Output ['ducati', 'honda', 'yamaha', 'flash', 'suzuki']

# delete and pop ()
'''del motorcycles3[1]
popped_moto = motorcycles3.pop()
print(motorcycles3)
print(popped_moto)'''

# pop() for print statement
last_owned = motorcycles3.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")
#Output: The last motorcycle I owned was a Suzuki.

# remove()
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
#Output: ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)
#Output: ['honda', 'yamaha', 'suzuki']

# remove() uses, my example

students = ['Ahsan', 'Marium', 'Waris', 'Ahmad']
print('Students in class = ',students)
Good = 'Waris'
students.remove(Good)
print(f'{students[0]} is good, but {Good.title()} is very good')
#Output: Students in class =  ['Ahsan', 'Marium', 'Waris', 'Ahmad']
Ahsan is good, but Waris is very good

# sort() Method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)  #Output: ['audi', 'bmw', 'subaru', 'toyota']
cars.sort(reverse=True)
print(cars)  #Output: ['toyota', 'subaru', 'bmw', 'audi']

# List sorting
'''print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)'''

# my own example

students2 = ['Ahsan', 'Marium', 'Waris', 'Sajal', 'Talha']
print('The original list of students is:')
print(students2)
print('\nAfter sorting list becomes: ')
print(sorted(students2))
print('\nReverse sortation of list: ')
students2.sort(reverse=True)
print(students2)
#Output:
The original list of students is:
['Ahsan', 'Marium', 'Waris', 'Sajal', 'Talha']

After sorting list becomes: 
['Ahsan', 'Marium', 'Sajal', 'Talha', 'Waris']

Reverse sortation of list: 
['Waris', 'Talha', 'Sajal', 'Marium', 'Ahsan']

# finding length of list
len(students2)
#oUtput: 5
