#SLICING IN PYTHON...

# a[start:stop]  # items start through stop-1
# a[start:]      # items start through the rest of the array
# a[:stop]       # items from the beginning through stop-1
# a[:]           # a copy of the whole array

numbers = [16,32,64,128,256,512,1024]
modified_numbers = numbers[0::2]
print(modified_numbers)

###############
names = ["Tom","Ben","Mike","Steve","Chad","Braxton"]
modified_names = names[slice(0,len(names),2)]
print(modified_names)


random_word = "bananas"
sliced_random_word = random_word[0:len(random_word):2]
print(sliced_random_word)

string_to_be_reversed_via_slicing = "Hellow World"
reversed_string = string_to_be_reversed_via_slicing[slice(None,None,-1)]
# OR YOU CAN DO....
#reversed_string = string_to_be_reversed_via_slicing[::-1]

# In this particular example, the slice statement [::-1] means start at the end of the string and end at position 0, move with the step -1, negative one, which means one step backwards.
print(reversed_string)

#============List Comprehension.....==============
# Start with brackets
# The General Format is: [___ for ___ in ___]
# "Perform THIS action on every *entity* in "blah" "

nums = [4,5,6]
doubled_numbers = ([x*2 for x in nums])
print(doubled_numbers,"\n")


colors = ['orange','green','purple','white']
capitalized_colors = [curr_color.upper() for curr_color in colors]
print(capitalized_colors,"\n")

even_nums = [2,4,6,8,10]
hello_evens = [f"Hello, {n}! ~~" for n in even_nums]
print(hello_evens,"\n")


list_of_nums = [1,2,3,4,5,6]
evens = [num for num in list_of_nums if num % 2 == 0]
odds = [num for num in list_of_nums if num % 2 != 0]
print(f"Odds: {odds} .....Evens:{evens}","\n")

####################################################
numbers = [1, 2, 3, 4, 5, 6]
evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0] 


####################################################
[num*2 if num % 2 == 0 else num/2 for num in numbers]
print(numbers,"\n")
# [0.5, 4, 1.5, 8, 2.5, 12]


####################################################
with_vowels = "This is so much fun!"
without_vowels = ''.join(char for char in with_vowels if char not in "aeiou")
print(without_vowels,"\n")
# "Ths s s mch fn!"


####################################################
names = ["Ellie","Tim","Matt"]
answer = [name[0] for name in names]
print(answer,"\n")

####################################################
num_list = [1,2,3,4,5,6]
answer2 = [num for num in num_list if num % 2 == 0]
print(answer2,"\n")


####################################################
list_1 = [1,2,3,4]
list_2 = [3,4,5,6]
answer = [num for num in list_1 if num in list_2]
print (answer,"\n")


####################################################
# Given a list of names, create a variable called answer2, which is a new list with each name reversed and in lower case.
list_of_names = ["Ellie","Tim","Matt"]
#the slice [::-1] is a quick way to reverse a string
answer2 = [name[::-1].lower() for name in list_of_names]
print(answer2)

####################################################
# For all the numbers between 1 and 100 (including 100), create a variable called ANSWER, which contains a list with all the numbers thar are divisible by 12.

my_range = range(1,101)
answer = [num for num in my_range if num % 12 == 0]
print(answer)

####################################################
# Given the string 'amazing', create a variable called answer which is a list containing all the letters from 'amazing' except without any vowels.

amazing_string = 'amazing'
answer = [letter for letter in amazing_string if letter not in('aeiou')]
print(answer)

####################################################
# Using List Comprehension and range(), create a variable called answer with the following value - [[0,1,2],[0,1,2],[0,1,2]]

answer = [[var for var in range(0,3)] for x in range(0,3)]
print(answer)


####################################################
# Using list comprehension, create a v ariable called answer with the following value:
# [
# 	[0,1,2,3,4,5,6,7,8,9],
# 	[0,1,2,3,4,5,6,7,8,9],
# 	[0,1,2,3,4,5,6,7,8,9],
# 	[0,1,2,3,4,5,6,7,8,9],
# 	[0,1,2,3,4,5,6,7,8,9],
# 	[0,1,2,3,4,5,6,7,8,9],
# 	[0,1,2,3,4,5,6,7,8,9],
# 	[0,1,2,3,4,5,6,7,8,9],
# 	[0,1,2,3,4,5,6,7,8,9],
# 	[0,1,2,3,4,5,6,7,8,9]
# ]
# It's a 10x10 nested list. 10 rows, each row contains the numbers 0-9.
answer = [[num for num in range(0,10)] for x in range(1,11)]
print(answer)



# ~~~~~~~*****RECAP!!*****~~~~~~~
# lists are fundamental data structures for ordered information
# lists can be include any type, even other lists!
# we can modify lists using a variety of methods
# slices are quite useful when making copies of lists
# list comprehension is used everywhere when iterating over lists, strings, ranges and even more data types!
# nested lists are essential for building more complex data structures like matrices, game boards and mazes
# swapping is quite useful when shuffling or sorting