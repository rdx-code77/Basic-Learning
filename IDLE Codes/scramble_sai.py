'''
    Author: Saikumar Srinivas
    Filename: scramble_sai.py
    Purpose: Scrambled Words
    The source code below defines four encoded common English words.
    Each word is 7 letters long.
    Reveal the words by writing Python code to sort the list by the
    integer value in each tuple.
    Use lambda constructs and list comprehensions in your solution.
'''
z = [('v', 'c', 'l', 6, 'r'), ('i', 'a', 'i', 4, 't'),
     ('a', 'f', 'g', 1, 'p'), ('h', 'n', 'r', 3, 's'),
     ('e', 'e', 'a', 7, 'e'), ('c', 'i', 'o', 2, 'a'),
     ('e', 'n', 'l', 5, 'u')]


# Step 1:   Sort the tuples based on the integer value in each.  Use a
#           lambda construct to provide the sort key.
z.sort(key=lambda a: a[3])

# Step 2:   Use a list comprehension to create a list of characters
#           for each word.
word1 = [a[0] for a in z]
word2 = [a[1] for a in z]
word3 = [a[2] for a in z]
word4 = [a[4] for a in z]

# Step 3:   Use the join() method to create a string for each of the
#           four words and print them.
word1 = ''.join(word1)
word2 = ''.join(word2)
word3 = ''.join(word3)
word4 = ''.join(word4)

print("Word1 = {}".format(word1))
print("Word2 = {}".format(word2))
print("Word3 = {}".format(word3))
print("Word4 = {}".format(word4))


