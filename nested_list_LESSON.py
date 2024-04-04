# A nested list is a list that contains another list (i.e.: a list of lists). It is also referred to as a multi-diminsional array. For example, a 2 dimensional array is used below:

nested_list = [['blue', 'green'], ['red', 'black'], ['blue', 'white']]
print len(nested_list)
# prints 3
print nested_list[1]
# prints ['red', 'black']
print nested_list[1][0]
# prints red
#To go through every element in this list, use a nested for loop.

>>> nested_list = [['blue', 'green'], ['red', 'black'], ['blue', 'white']]
>>> for inner in nested_list:
...     for value in inner:
...         print value
... 
#blue
#green
#red
#black
#blue
#white
