# Week 9 Notes

# Chapter 10 - Dictionaries
# https://thartmanoftheredwoods.github.io/CIS-12/week_9py.html

# Declarations
'''
student = {
    'name': 'Alice',
    'age': 22,
    'major': 'Computer Science'
}
# print(student['name'])  # Outputs: Alice
'''
# or

# grades = {'Alice': 'A', 'Bob': 'B', 'Charlie': 'C'}
# print(grades['Bob'])  # Outputs: B

# built-In Function convertion to dictionary

list_of_tuples = [('apple', 3), ('banana', 6), ('cherry', 5)]
fruit_counts = dict(list_of_tuples)
# print(fruit_counts)  # Outputs: {'apple': 3, 'banana': 6, 'cherry': 5}

# in Operator concerning dictionaries
'''
country_codes = {'US': 1, 'IN': 91, 'JP': 81}
if 'JP' in country_codes:
    print('Country code for Japan is:', country_codes['JP'])
'''
# Updating and Modifying Dictionaries

phone_book = {'Alice': '555-1234', 'Bob': '555-5678'}
del phone_book['Alice']  # Removes Alice
phone_book['Charlie'] = '555-8765'  # Adds Charlie
# print(phone_book)  # Outputs: {'Bob': '555-5678', 'Charlie': '555-8765'}

# Looping thru Dictionaries
'''
color_codes = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF'}
for color, code in color_codes.items():
    print(f'{color}: {code}')
'''
# Counting with Dictionaries

def count_characters(string):
    counts = {}
    for char in string:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

# print(count_characters('abracadabra'))

# using dictionaries for memoization

memo = {0: 0, 1: 1}

def fibonacci(n):
    if n in memo:
        return memo[n]
    memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo[n]

# print(fibonacci(10))  # Outputs: 55

# Exercises

# Word Frequency Counter

def count_words(text):
    counts = {}
    for word in text.split():
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

# print(count_words('hello hello world hello'))

# Student Grades

report_card1 = {'Douglas':'B', 'Gaiman':'A', 'Pratchett': 'C'}

def highest(report_card):
    return sorted(report_card.items(), key=lambda item: item[0], reverse=True)

# print(highest(report_card1))

report_card2 = {'Atilla':95,'Charlemagne':84,'Alexander':92}

def top_student(report_card):
    max_grade = 0
    name = ''
    for student, grade in report_card.items():
        if grade > max_grade:
            max_grade = grade
            name = student
    return name

# print(top_student(report_card2))

# Filtering Long Words
'''
def words_by_len(text):
    string = dict(count_words(text))
    if string.item() = 1:
        pass
    print(string)
    return count_characters(string)

def words_by_len_v2(text):
    word = text.split()
    len_dict = {}
    for word in text:
        word_len = len(word)
        if word_len not in len_dict:
            len_dict[word_len] = {}
        len_dict[word_len].append(word)
'''
text = 'hello world and also the universe and such'
# print(words_by_len_v2(text))

# print(words_by_len(text))

# Chapter 11 - Tuples
# https://thartmanoftheredwoods.github.io/CIS-12/week_9ch11py.html

# Tuple with a single element
one_element_tuple = ('only',)  # NOTE: the ending comma IS necessary to make it a tuple.
# print(f"Type of one_element_tuple: {type(one_element_tuple)}")

# Concatenation and repetition
new_tuple = one_element_tuple + ('element',)
repeated_tuple = new_tuple * 3
# print(repeated_tuple)

# tuples as immutable objects
location_dict = {('Eureka', 'California'): 'Foggy', ('Las Vegas', 'Nevada'): 'Sunny'}
# print(location_dict[('Eureka', 'California')])  # Using a tuple as a dictionary key

# Swapping values using tuple assignment
x, y = 5, 10
x, y = y, x
# print(f"x: {x}, y: {y}")

# tuples as return values
def get_min_max(numbers):
    return min(numbers), max(numbers)

result = get_min_max([10, 5, 3, 9, 2])
# print(f"Min: {result[0]}, Max: {result[1]}")

# packing and unpacking arguments
def multiply_all(*numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# print(multiply_all(2, 3, 4))  # Unpacking variable arguments

# zip function (sequences must be the same length or will error)
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 78]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")

# comparing and sorting tuples
students = [('Alice', 85), ('Bob', 90), ('Charlie', 78)]
sorted_students = sorted(students, key=lambda student: student[1], reverse=True)
print(f"Top student: {sorted_students[0][0]}")

# exercises

# reverse your favorite foods
def rev_fav_foods(tuple_in):
    return tuple_in[::-1]

fav_foods = ('cheese','chocolate','soda','apple','pizza','strawberry')
print(rev_fav_foods(fav_foods))

# using zip exercise

keys = ['a','b','c']
values = [1,2,3]

# combine and print
for key, value in zip(keys,values):
    print(f"{key},{value}")

# make it a dictionary (simple version)
new_dict = dict(zip(keys,values))
print(new_dict)

# other method
def build_dict(keys,values):
    result = {}
    for k,v in zip(keys,values):
        result [k] = v
    return result

# or
def build_dict_v2(keys,values):
    return { k:v for k,v in zip(keys,values) }


