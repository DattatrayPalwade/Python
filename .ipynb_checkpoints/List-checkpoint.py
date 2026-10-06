"""
*******************************************************************************
Filename  : List.py
Author    : Dattatray Palwade - Value Tech Academy
*******************************************************************************

===============================================================================
Python List Data Type
---> List is a mutable, ordered collection of objects.
===============================================================================

# Key characteristics:
- Ordered: Elements maintain their insertion order.
- Mutable: Elements can be added, removed, or modified.
- Allows duplicates: The same value can appear multiple times.
- Heterogeneous: A list can contain different data types.
- Zero-indexed: The first element is accessed using index 0.

# Important properties:
Ordered       → maintains element order
Mutable       → elements can be changed
Index-based   → elements accessed using index
Dynamic       → size can grow/shrink
Duplicates    → allowed
Heterogeneous → different types can be stored
    
"""


"""============================================================================
Creating lists: 
Syntax --->
    list_name = [item1 , item2 , item3 , item4]
============================================================================"""
# 1. List with values
li_values = [ 10, 20 , 30 , 40 , 50 ]          
print(li_values)

# 2. Empty list
li_empty = []         
print(li_empty)

# 3. Using list()
text = "Dattatray"
char_list = list(text)
print(char_list) 

text = "Shree Swami Samarth !..."
li = list(map( str , text.split(" ")))
print(li)

# 4. Repeated values
zeros = [0] * 5
print(zeros)


"""============================================================================
Display lists:
============================================================================"""
# 1. Using print() Function
li = [ 10 , 20 , 30 , 40 , 50 ]
print(li)

# 2. Iterating with a for Loop
li = [ 10 , 20 , 30 , 40 , 50 ]

for i in li :
    print(i)

# 3. Using the Unpacking Operator (*)
li = [ 10 , 20 , 30 , 40 , 50 ]
print(*li)
print(*li , sep="\n")

# 4. Using the .join() String Method
li = [ 10 , 20 , 30 , 40 , 50 ]
print(",".join(map( str , li)))

# 5. Using enumerate() for Indexed Display

# --------------------------------------------------------------------------- #

"""============================================================================
Taking List as Input:
============================================================================"""

# --------------------------------------------------------------------------- #

"""============================================================================
Indexing: It is used to access elements from the list.
Syntax ---> 
    list_name[index]
============================================================================"""
# 1. Forward indexing ( Starting index - 0 , End index - n-1 )
li = [ 10 , 20 , 30 , 40 , 50 ]
index = li[0]   # 
print(index)






# --------------------------------------------------------------------------- #





######################### DO NOT EDIT BELOW THIS LINE #########################
