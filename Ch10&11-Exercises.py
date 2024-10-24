# Exercises from Ch 10 and 11
# assignment: https://redwoods.instructure.com/courses/18740/assignments/441529?module_item_id=996659

# Ch 10 - Dictionaries - Exercises

#Ex2

def value_counts_efficient(string):
    counter = {}
    for letter in string:
        counter[letter] = counter.get(letter,0) + 1
    return counter

print(value_counts_efficient('llama'))

#Ex3

def has_duplicates(word):
    return len(value_counts_efficient(word).keys()) != len(word)

print(has_duplicates('unpredictably'))
print(has_duplicates('unpredictable'))

#Ex4

def find_repeats(counter):
    """Makes a list of keys with values greater than 1.

    counter: dictionary that maps from keys to counts

    returns: list of keys
    """
    return [k for k,v in counter.items() if v > 1]

print(find_repeats(value_counts_efficient('brontosaurus')))

#Ex5

counter1 = value_counts_efficient('brontosaurus')
counter2 = value_counts_efficient('apatosaurus')

def add_counters(dict1,dict2):
    result = dict(dict1)
    for k, v in dict2.items():
        result[k] = result.get(k, 0) + v
    return result

print(add_counters(counter1,counter2))

#Ex6

def load_word_dict(file_path):
    word_dict = {}
    with open(file_path, 'r') as word_file:
        for word in word_file:
            word_dict[word.strip().lower()] = True
    return word_dict

new_dict = load_word_dict('files/words.txt')

def is_interlocking(word, word_dict):
    word = word.lower()
    first = word[0::2]
    second = word[1::2]
    return first in word_dict and second in word_dict

print(is_interlocking('schooled', new_dict))
print(is_interlocking('brontosaurus', new_dict))

# Chapter 11 - Tuples - Exercises

# Ex2

list0 = [1, 2, 3]
list1 = [4, 5]

t = (list0, list1)
t[1].append(6)
print(t)

# Ex3

letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = range( len( letters ) )
letter_map = dict( zip( letters, numbers ) )

def shift_word(word, shift):
    cipher_text = ''
    for l in word:
        l_index = (letter_map[l] + shift) % len(letters)
        cipher_text += letters[l_index]
    return cipher_text

print(shift_word('cheer',7))
print(shift_word('melon',16))

# Ex4 TODO: still working on these last few exercises

def most_frequent_letters(word):
    counter = value_counts_efficient(word)
    return sorted(counter.items())

print(most_frequent_letters('brontosaurus'))

#Ex5

def anagram_sets(file_path):
    pass

#Ex6

def word_distance(word1,word2):
    pass

#Ex7

def metathesis_pairs(file_path):
    pass

