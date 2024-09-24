'''
Author: Saikumar Srinivas
Filename: doubleScramble_sai.py
Purpose: Double Scrambled Words
    The variable z contains four encoded common English words.
    Each word is 5 letters long.
    Reveal the words by writing Python code to sort the list by the
    integer value in each tuple.
    Use lambda constructs and list comprehensions where possible.
    *** Note that unlike the previous problem, each item in z is a list.
        Each list has an integer that encodes the position in a different
        location in the list.  The characters are in the correct order but
        you will need to rotate each list so the integers are in the same
        location in each list.  The most convenient location would be at
        index zero because then, you would not need to provide a sort key.
    Example: rotate z[0] so it looks like this: [3, 't', 'n','s', 'a']
'''

z = [['s', 'a', 3, 't', 'n'],['h', 'b', 'c', 1, 'p'],
     ['h', 'y', 'c', 'k', 5],[4, 'c', 'e', 'i', 'l'],
     ['o', 'a', 'h', 2, 'i']]

# Step 1:   Rotate each list in z so the integer is in the zero position
#           without changing the order of the characters.
def rotate(Z):
	for i in range(len(Z)):
		if(type(Z[i])==int):
			return i
	return -1

z = [a[rotate(a):]+a[:rotate(a)] for a in z]

# Step 2:   Sort the lists based on the integer value in each.
z.sort(key = lambda i: i[0])

# Step 3:   Use a list comprehension to create a list of characters
#           for each word.
word1 = [a[1] for a in z]
word2 = [a[2] for a in z]
word3 = [a[3] for a in z]
word4 = [a[4] for a in z]

# Stpe 4:   Use the join() method to create a string for each of the
#           four words and print them.
word1 = ''.join(word1)
word2 = ''.join(word2)
word3 = ''.join(word3)
word4 = ''.join(word4)

print("Word1 = {}".format(word1))
print("Word2 = {}".format(word2))
print("Word3 = {}".format(word3))
print("Word4 = {}".format(word4))
