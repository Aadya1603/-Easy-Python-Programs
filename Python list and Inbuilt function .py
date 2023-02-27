#Python provides several built-in data structures for organizing and manipulating data,
# including lists, dictionaries, and sets.

#LIST
#   A list is an ordered collection of elements, which can be of any type. Lists are mutable,
#   meaning that you can change the order of the elements, add or remove elements, or modify the values
#   of elements. Lists are created using square brackets and individual elements are separated by commas.

#Class of List
print(type([]))


#Print Empty list 
lst_example=[]
print(lst_example)


#list
lst=[1,2,3,4,"Cars"]
print(lst)

#Iterating list
lst=[1,2,3,4,5,6]
for i in lst:
    print(i**2)

#In build function 
print(len(lst))

lst=[1,2,3,4,5]
lst.append("Cars")
print(lst)

#Indexing
print(lst[5])
print(lst[0])
print(lst[3])
print(lst[:])
print(lst[2:])
print(lst[:4])
print(lst[3:5])


#operation on List 
print(lst*3)
print(lst.pop(2))
print(lst)
print(lst.count(4))


#SETS
#   A set is an unordered collection of unique elements. Sets are mutable and can be modified using
#   a variety of set operations, such as adding or removing elements, or finding the intersection or 
#   union of two sets. Sets are created using curly braces, with individual elements separated by commas.


#to check default set
print(type({1,2,3,4,5}))

#Defining an empty set 
set_1=set()
print(set_1)
print(type(set_1))

#Inbuilt function on sets 
set_1.add("Cars")
print(set_1)

set_1.update("Something")
print(set_1)
#it will print in unordered way because ( A set is an unordered collection of unique elements.)
set_2={1,2,3,4,5}
print(set_2)

set_2.add("Cars")
print(set_2)

c=set_2.issuperset(set_1)
print(c)




#DICTIONARY
#   A dictionary is an unordered collection of key-value pairs, where each key is unique. 
#   Dictionaries are mutable and can be modified in the same way as lists. Dictionaries are created
#   using curly braces, with each key-value pair separated by a colon and individual pairs separated 
#   by commas.


#Type 
print(type({4:"cars"}))

#Defining Dictionary

print(dict(carname="Audi" ,Model=73682,carbarnumber="a3f5k94"))


#Indexing in Dictionary 

my_dict={"car1":"Audi","car2":"BMW","car3":"swift"}
print(type(my_dict))

print(my_dict["car1"])
print(my_dict["car3"])
print(my_dict["car2"])

#In built function
print(my_dict.keys)
print(my_dict.items)


#Using loops in Dictionary 

for x in my_dict:
    print(x)

for x in my_dict.values():
    print(x)

for x in my_dict.items():
    print(x)


#Adding more item to to Dictionary

my_dict["car4"]="volvo"
print(my_dict)


#Nesting in Dictionary 

# Add keys and values to the inner dictionaries

nested_dict = {}

nested_dict['outer_key1'] = {}
nested_dict['outer_key2'] = {}

nested_dict['outer_key1']['inner_key1'] = 'value1'
nested_dict['outer_key1']['inner_key2'] = 'value2'
nested_dict['outer_key2']['inner_key3'] = 'value3'

print(nested_dict)


#TUPLE
#A tuple is a collection of ordered, immutable, and heterogeneous elements enclosed in parentheses (). 
#Tuples are similar to lists, but they have some key differences.

#One of the main differences between tuples and lists is that tuples are immutable,
#which means their values cannot be changed once they are created. This makes tuples useful when 
#you need to store a fixed set of values that should not be modified.

#Tuples are also often used for returning multiple values from a function, 
#since you can group those values together into a single tuple and return it. Tuples can be accessed 
#using indexing, slicing, and looping, just like lists.


# Creating a tuple
my_tuple = ('apple', 'banana', 'cherry')

# Accessing tuple elements
print(my_tuple[0])  # Output: 'apple'
print(my_tuple[1])  # Output: 'banana'
print(my_tuple[2])  # Output: 'cherry'

# Looping through a tuple
for item in my_tuple:
    print(item)

# Slicing a tuple
print(my_tuple[1:])  # Output: ('banana', 'cherry')
