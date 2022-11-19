
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

print(dict['movies'])   # o/p -('GI-Joe', 'sky') --- List
# print secondary movie 
print(dict['movies'][1])    # o/p -- sky


print(dict['State_visited'])  # o/p -- {'punjab', 'Haryana'}-- Set
#print(dict['State_visited'][1])  # o/p --- TypeError: 'set' object is not subscriptable


print(dict['movies'][0])    # o/p -- GI-Joe

print(dict['City'])         # o/p -- vidisha

print(dict['other_var'])    # o/p -- {'Fruit': 'Apple', 'Animal': 'Rabit', 'Sport': 'Cricket'}   -- This is a dictionary kind of output

#print(dict['other_var'][1])     # o/p -- KeyError: 1
            # This is because the value assigned to key "other_var" is dictionary and on dictionary, method of indexing can't be applicable. 


# with the help of indices we can access nested elements of list, tuple only but same way is not applicable on dictionary.

# So let me show you how we print value of specific key from dictionary nested in some other dictionary
print(dict['other_var']['Animal'])      # o/p -- Rabit

print(dict['other_var']['Fruit'])       # o/p -- Apple

print(dict['other_var']['Sport'])       # o/p --- Cricket



# Let's see the syntax for updatting the distionary 
        # Dictionar_name['Key'] = 'New_value'    This way we can assigne/update any key of dictionary by new value.

print(dict)
dict['Name'] = 'Ankita'
print(dict)

dict['Age'] = 28
print(dict)


dict['skills'] = 'python'
print(dict)

# Let's find out how to print only keys of our dictionary
#print(dict('key'))              # TypeError: 'dict' object is not callable

'''All_key = dict.keys()
print(All_key)          # o/p -- dict_keys(['Name', 'Age', 'skills', 'state', 'City', 'State_visited', 'movies', 48, 'other_var'])
'''

print("All the keys used in our dictionary are: ",dict.keys())
    # o/p --- All the keys used in our dictionary are:  dict_keys(['Name', 'Age', 'skills', 'state', 'City', 'State_visited', 'movies', 48, 'other_var'])

# Similarly we can also get the all values only of dict
print(dict.values())
'''# o/p --- dict_values(['Ankita', 28, 'python', 'M.P.', 'vidisha', {'Haryana', 'punjab'}, 
    # ('GI-Joe', 'sky'), 'Virat_jersey', {'Fruit': 'Apple', 'Animal': 'Rabit', 'Sport': 'Cricket'}])
'''


# Let's see how to calculate toatal no. of keys use in dictionary
'''x = (int)(dict.keys())
print(x)        # o/p -- TypeError: int() argument must be a string, a bytes-like object or a number, not 'dict_keys'
'''

# Let's see how to iterate on dictionary

for k,v in dict.items():
    print("Key is",k, 'and', 'Value is',v)



# Let's see how to compare 2 dictionary.
dict2 = {'a':1, 'b':2, 'c':3}
dict3 = {'b':2, 'c':3, 'a':1}
print(dict2 == dict3)           # o/p -- True
        # Hence dictionary is not a sequential data type proved. 
        # So, basicaly if key-value pair are same in both the dictionary, then it doesn't matter if the order are in same sequence or not.


dict1_1={'d':4, 'e':5, 'f':6}
dict1_2={'d':4, 'e':7, 'f':6}
print(dict1_1==dict1_2)             # o/p --- False



# Let's see how to delete a specific key-value pair from dictionary
            # for this we can use keyword "del" and it will delete specific key-value pair from dictionary as well as its references. 
           # Syntax -- del dictionary_name['key'] --- enter that key which you want to remove from your dictionary and the corresponding value will also get vanished.

print(dict)
# if suppose i want to delete the key age and its value
del dict['Age']
print(dict)

del dict[48]
print(dict)




# Let's see how to verify weather a particular key in our dictionary exist or not?
            # syntax -- print(dictionary_name.has_key['Key_name']) --- Here, key_name is the name of key which we want to check exist or not.
'''
print(dict.has_key('Skills'))           # o/p -- AttributeError: 'dict' object has no attribute 'has_key'
                            # Maybe  ".has_key" -- doesn't work on this version python3.0 and maybe work on python2.0 
'''
 

 # Another way of verifying presence of key in our dictionay ----  ".get('key')"
print(dict.get('Skills'))           # o/p -- None because instead of lowercase s we write uppercas S in string skills and we know python is a case-sensitive language. 

print(dict.get('skills'))       # o/p --- python


# Another alternative approaach for checking the keys
keys_in_dict = list(dict.keys())
'''if 'skills' in keys_in_dict:
   print(Yes)                  # o/p ----- NameError: name 'Yes' is not defined
else:
    print(No)'''

if 'skills' in keys_in_dict:
    print(True)
else:
    print(False)
                            # O/p --- True














































































