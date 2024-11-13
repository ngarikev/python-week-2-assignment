#Created an empty list called my_list
my_list = []

#appending multiple elements to an empty list

my_list.extend((20, 10, 30, 40))

#Inserting the value 15 at the second position in the list.
my_list.insert(1, 15)

#Extend my_list with another list: [50, 60, 70].
new_list = [50, 60, 70]

my_list.extend(new_list)

#Remove the last element from my_list.
my_list.remove(70)
    #OR
del my_list[-1]

#Sort my_list in ascending order.
my_list.sort()

#Find and print the index of the value 30 in my_list.
print(my_list.index(30))
