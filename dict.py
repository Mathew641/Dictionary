
#Dictionary creation and understanding

# Dictionary --- Another data type in python.
# Dictionary in python acts like a MAp data structure (key - value kind of structure.)

# Syntax of dictionary --  {
                        
                        # 'key' : 'Value' 
                         
                         # }

# Eg --  Dict = {'Name':'Abhishek', 'Age':'31', 'skills':'C', 'color':'White'}
    # here Dict is a variable in which key-value pair stored i.e. dictionary is stored.

# Key -- key can be a string or int but CANNOT by list, tuple, set etc. (i.e any iterable data which cannot be used as mapping structure cannot be use as key)
# Value -- Value can be anything such as list, string, int, float, nested list etc.
# Means for key we have some restriction but vot for value, means anything can be assigned to key.


# Let's see how can we create dictionary and play with it means apply certain operation on top of it.

dict = {}   # It is an empty dictiionary.
#This is qan empty list and let's check the data type for it 
print(type(dict))   # --- o/p -- <class 'dict'>

# Dictionary is not a kind of sequential data structure, hence its data cannot be access with the help of indices, like in case of list, string, tuple which are sequential data structure.

# We can access value in dictionary only if we knew the key.


# Let's see how can we insert key-value pair in dictionary

dict['Name'] = 'Abhishek'
dict['Age'] = 31
dict['skills'] = 'C'
dict['state'] = "M.P."
dict['City'] = 'vidisha'

#print(dict)

# Way of inserting key value pair in dictionary --  Dictionary_name['Key'] = 'Value'

dict[48] = 'Virat_jersey'
print(dict) # o/p -- {'Name': 'Abhishek', 'Age': 31, 'skills': 'C', 'state': 'M.P.', 'City': 'vidisha', 48: 'Virat_jersey'}

# Even we can put dictionary inside dictionary
dict['other_var'] = {'Fruit':'Apple', 'Animal':'Rabit', 'Sport':'Cricket'}

print(dict)
''' # O/P --- {'Name': 'Abhishek', 'Age': 31, 'skills': 'C', 'state': 'M.P.', 'City': 'vidisha', 48: 'Virat_jersey', 
'dict1': {'Fruit': 'Apple', 'Animal': 'Rabit', 'Sport': 'Cricket'}}
'''






























#Dictionary creation and understanding

# Dictionary --- Another data type in python.
# Dictionary in python acts like a MAp data structure (key - value kind of structure.)

# Syntax of dictionary --  {
                        
                        # 'key' : 'Value' 
                         
                         # }

# Eg --  Dict = {'Name':'Abhishek', 'Age':'31', 'skills':'C', 'color':'White'}
    # here Dict is a variable in which key-value pair stored i.e. dictionary is stored.

# Key -- key can be a string or int but CANNOT by list, tuple, set etc. (i.e any iterable data which cannot be used as mapping structure cannot be use as key)
# Value -- Value can be anything such as list, string, int, float, nested list etc.
# Means for key we have some restriction but vot for value, means anything can be assigned to key.


# Let's see how can we create dictionary and play with it means apply certain operation on top of it.

dict = {}   # It is an empty dictiionary.
#This is qan empty list and let's check the data type for it 
print(type(dict))   # --- o/p -- <class 'dict'>

# Dictionary is not a kind of sequential data structure, hence its data cannot be access with the help of indices, like in case of list, string, tuple which are sequential data structure.

# We can access value in dictionary only if we knew the key.


# Let's see how can we insert key-value pair in dictionary

dict['Name'] = 'Abhishek'
dict['Age'] = 31
dict['skills'] = 'C'
dict['state'] = "M.P."
dict['City'] = 'vidisha'
dict['State_visited'] = {'punjab', 'Haryana'}
dict['movies'] = ('GI-Joe', 'sky')
#print(dict)

# Way of inserting key value pair in dictionary --  Dictionary_name['Key'] = 'Value'

dict[48] = 'Virat_jersey'
print(dict) # o/p -- {'Name': 'Abhishek', 'Age': 31, 'skills': 'C', 'state': 'M.P.', 'City': 'vidisha', 48: 'Virat_jersey'}

# Even we can put dictionary inside dictionary
'''dict1 = {'Fruit':'Apple', 'Animal':'Rabbit', 'sports':'Cricket'}
dict['other_things'] = dict1
print(dict)'''

dict['other_var'] = {'Fruit':'Apple', 'Animal':'Rabit', 'Sport':'Cricket'}

print(dict)
''' # O/P --- {'Name': 'Abhishek', 'Age': 31, 'skills': 'C', 'state': 'M.P.', 'City': 'vidisha', 48: 'Virat_jersey', 
'dict1': {'Fruit': 'Apple', 'Animal': 'Rabit', 'Sport': 'Cricket'}}
'''

# How to check length of dictionary ?
print('Length of dictionary is: ',len(dict))  # o/p -- Length of dictionary is:  9
# Basicaly length of dictionary is equal to the No. of key-value pair.


# How to access the value of particular key?
print(dict['Name'])      # O/p -- Abhishek           

print(dict['other_var'])        # O/p -- {'Fruit': 'Apple', 'Animal': 'Rabit', 'Sport': 'Cricket'}

print(dict['State_visited'])        # O/p -- {'Haryana', 'punjab'}

print(dict['skills'])           # O/p -- C
















































































