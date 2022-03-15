#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''Question 1:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated
sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24'''

import math
number = input("Provide D: ")
number = number.split(',')
print(number)

l1 = []
for D in number:
    Q = math.sqrt(2*50*int(D)/30)
    Q = round(Q) #---> It will roundoff the outcoming values of Q
    l1.append(Q)
print(l1)
    


# In[ ]:





# In[3]:


'''Question 2:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The
element value in the i-th row and j-th column of the array should be i*j.
Note: i = 0,1,....., X-1
      j = 0,1,....., Y-1
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]'''

X = 3
Y = 5
list = [[0 for col in range(Y)] for row in range(X)]

for row in range(X):
    for col in range(Y):
        list[row][col]= row*col
print(list)


# In[4]:


'''Question 3:
Write a program that accepts a comma separated sequence of words as input and prints the
words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world'''

css = input("Enter the css: ")
spl = css.split(",")
spl.sort()
print(','.join(spl))


# In[10]:


'''Question 4:
Write a program that accepts a sequence of whitespace separated words as input and prints
the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
'''
seq1 = input("Enter a sequence:\n")
word = seq1.split(" ")
emp_list = []
for i in word:
    if i not in emp_list:
        emp_list.append(i)
emp_list.sort()
seq2 = ' '.join(emp_list)
print(seq2)
        


# In[14]:


'''Question 5:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3'''

sen = input("Enter a sentence:\n")
LETTERS = 0
DIGITS = 0
list = []
for i in sen:
    if i.isdigit():
        DIGITS += 1
    elif i.isalpha():
        LETTERS += 1
    else:
        pass
print(f"DIGITS = {DIGITS}")
print(f"LETTERS = {LETTERS}")


# In[35]:


'''Question 6:
A website requires the users to input username and password to register. Write a program to
check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them
according to the above criteria. Passwords that match the criteria are to be printed, each
separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
'''

import re
password = input("Enter a password:\n")
password = password.split(",")
accepted_pass = []
for i in password:
    if len(i)<6 or len(i)>12:
        continue
    elif not re.search("[a-z]", i):
        continue
    elif not re.search("[A-Z]", i):
        continue
    elif not re.search("[0-9]", i):
        continue
    elif not re.search("[!@#$%^&]",i):
        continue
    else:
        accepted_pass.append(i)
print((" ").join(accepted_pass))


# In[36]:


# TO DO
'''Question 7:
Define a class with a generator which can iterate the numbers, which are divisible by
7, between a given range 0 and n.'''


# In[58]:


'''Question 8:
Write a program to compute the frequency of the words from the input. The output
should output after sorting the key alphanumerically.
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or
Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
'''
import operator

text_line = input("Type in: ")

freq_dict = {}

for i in text_line.split(' '):
    if i.isalpha():  # ---> The isalpha() methods means if all characters in the string are alphabets or not.
        if i not in freq_dict:
            freq_dict[i] = 1
        elif i in freq_dict:
            freq_dict[i] = freq_dict[i] + 1
    else:
        pass

sorted_freq_dict = sorted(freq_dict.items(), key = operator.itemgetter(0))
print(sorted_freq_dict)

for i in sorted_freq_dict:
    print(i[0], i[1])


# In[10]:


'''
Question 9:
Please write a program to generate all sentences where subject is in [&quot;I&quot;, &quot;You&quot;] and
verb is in [&quot;Play&quot;, &quot;Love&quot;] and the object is in [&quot;Hockey&quot;,&quot;Football&quot;].'''

subject = ["I", "You"]
verb = ["Play", "Love"]
object = ["Hockey", "Football"]

def gen_sentence(subject,verb,object):
    for i in subject:
        for j in verb:
            for k in object:
                print(i , j, k)
subject = ["I", "You"]
verb = ["Play", "Love"]
object = ["Hockey", "Football"]
gen_sentence(subject,verb,object)


# In[16]:


'''Question 10:
Please write a program to compress and decompress the string "hello world!hello
world!hello world!hello world!".'''

import zlib  #---> zlib is a python library & it is basically used for data compressing byte like object.
s = b"hello world!hello world!hello world!hello world!"  #---> b is for creating a byte object.
print(len(s))

c = zlib.compress(s)
print(len(c))

d = zlib.decompress(c)
print(len(d))




# In[13]:


'''Question 11:
Please write a binary search function which searches an item in a sorted list. The
function should return the index of element to be searched in the list.
'''

l = [2, 5, 9, 1, 7, 6, 12]
l.sort()
print(f"Sorted list\n {l}")
def search_fxn(a):
    for i in l:
        if i == a:
            return l.index(a)
search_fxn(9)


# In[19]:


'''Question 12:
Please write a program using generator to print the numbers which can be divisible by 5 and
7 between 0 and n in comma separated form while n is input by console.
Example:
If the following n is given as input to the program:
100
Then, the output of the program should be:
0,35,70'''

n = int(input("Enter a number: "))
list = []
for i in range(0,n):
    if i==0:
        list.append(i)
    elif (i%5 == 0) and (i%7 == 0):
        list.append(i)
    else:
        continue
print(list)


# In[33]:


'''Question 13:
Please write a program using generator to print the prime numbers between 0 and n in comma
separated form while n is input by console.
Example:
If the following n is given as input to the program:
30
Then, the output of the program should be:
2, 3, 5, 7, 11, 13, 17, 19, 23, 29
'''

n = int(input("Enter a number: "))
list = []
for j in range(2,n):
    for i in range(2,j):
        if j%i ==0:
            break
        
    else:
        list.append(j)
print(list)
    
        


# In[35]:


'''Question 14:
Please write a program using generator to print the even numbers between 0 and n in comma
separated form while n is input by console.
Example:
If the following n is given as input to the program:
10
Then, the output of the program should be:
0,2,4,6,8,10'''

n = int(input("Enter the number: "))
list = []
for i in range(0,n+1):
    if i%2 ==0:
        list.append(i)
    else:
        continue
print(list)
        


# In[47]:


'''question 15:
The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program using list comprehension to print the Fibonacci Sequence in comma
separated form with a given n input by console.
Example:
If the following n is given as input to the program:
7
Then, the output of the program should be:
0,1,1,2,3,5,8,13
'''
n = int(input("Enter a number: "))
list = []
a = 0
b = 1
for i in range(0,n+1):
    if i < 0:
        print("Incorrect input")
    elif i == 0:
        list.append(a)
    elif i == 1:
        list.append(b)
    elif i>1:
        c = a + b
        a = b
        b = c
        list.append(b)
    else:
        continue
 
print(list)


# In[52]:


'''Question 16:
Please write a function to write the nth fibonacci number.
'''

n = int(input("The value of n is: "))
def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2,n+1):
            c = a + b
            a = b
            b = c
        return b
fibonacci(n)


# In[69]:


'''Question 17:
Assuming that we have some email addresses in the "username@companyname.com" format,
please write program to print the user name of a given email address. Both user names and
company names are composed of letters only.
Example:
If the following email address is given as input to the program:
john@google.com
Then, the output of the program should be:
john
'''
import re  #--->  re(Regular Expression), is a sequence of characters that forms a search pattern.

email = "john@google.com nitin@facebook.com rajat@ford.com"
pattern = "(\w+)@\w+.com"
ans = re.findall(pattern,email)  #--->findall() means finds all the matches and returns them as a list of strings, with each string representing one match.
pattern2 = "\w+@(\w+).com"
ans2 = re.findall(pattern2,email)
print(ans)
print(ans2)


# In[3]:


''' Question 18:
Write a function that stutters a word as if someone is struggling to read it. The
first two letters are repeated twice with an ellipsis ... and space after each, and then the
word is pronounced with a question mark ?.
Examples
stutter("incredible") ➞ "in... in... incredible?";
stutter("enthusiastic") ➞ "en... en... enthusiastic?"
stutter("outstanding") ➞ "ou... ou... outstanding?"

Hint :- Assume all input is in lower case and at least two characters long.
'''

def stutter(word):
    s = word[0:2]
    return (2 * (s + "...") + word + "?")

print(stutter("incredible"))
print(stutter("enthusiastic"))
print(stutter("outstanding"))


# In[14]:


'''Question 19:
Create a function that takes an angle in radians and returns the corresponding
angle in degrees rounded to one decimal place.
Examples
radians_to_degrees(1) ➞ 57.3
radians_to_degrees(20) ➞ 1145.9
radians_to_degrees(50) ➞ 2864.8
'''
import math
from math import pi

def radian(r):
    d = r*(180/pi)
    return (round(d,1))  #---> Roundoff till first place.

print(radian(1))
print(radian(20))
print(radian(50))


# In[16]:


'''Question 20:
In this challenge, establish if a given integer num is a Curzon number. If 1 plus
2 elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is a Curzon
number.
Given a non-negative integer num, implement a function that returns True if num is a Curzon
number, or False otherwise.
Examples
is_curzon(5) ➞ True
# 2 ** 5 + 1 = 33
# 2 * 5 + 1 = 11
# 33 is a multiple of 11
is_curzon(10) ➞ False
# 2 ** 10 + 1 = 1025
# 2 * 10 + 1 = 21
# 1025 is not a multiple of 21
is_curzon(14) ➞ True
# 2 ** 14 + 1 = 16385
# 2 * 14 + 1 = 29
# 16385 is a multiple of 29'''

def is_curzon(n):
    a = 2**n + 1
    b = 2*n + 1
    if a%b == 0:
        return True
    else:
        return False
print(is_curzon(5))
print(is_curzon(10))
print(is_curzon(14))


# In[33]:


'''Question 21:
Question 4.Given the side length s. find the area of a hexagon.
Area(A) = [(3 * (3**(1/2))/2) * (s**2)]
Examples
area_of_hexagon(1) ➞ 2.6
area_of_hexagon(2) ➞ 10.4
area_of_hexagon(3) ➞ 23.4'''


def area_hexagon(s):
    c = (3 * (3**(1/2))/2)
    a = c * (s**2)
    return (round(a,1))

print(area_hexagon(1))
print(area_hexagon(2))
print(area_hexagon(3))


# In[52]:


'''Question 22:
Create a function that returns a base-2 (binary) representation of a base-10
(decimal) string number. To convert is simple: ((2) means base-2 and (10) means base-10)
010101001(2) = 1 + 8 + 32 + 128.
Going from right to left, the value of the most right bit is 1, now from that every bit to the left
will be x2 the value, value of an 8 bit binary numbers are (256, 128, 64, 32, 16, 8, 4, 2, 1).
Examples
binary(1) ➞ "1"
# 1*1 = 1
binary(5) ➞ "5"
# 1*1 + 1*4 = 5
binary(10) ➞ "10"
# 1*2 + 1*8 = 10'''


# In[35]:


'''Question 23:
Create a function that takes three arguments a, b, c and returns the sum of the
numbers that are evenly divided by c from the range a, b inclusive.
Examples
evenly_divisible(1, 10, 20) ➞ 0
# No number between 1 and 10 can be evenly divided by 20.
evenly_divisible(1, 10, 2) ➞ 30
# 2 + 4 + 6 + 8 + 10 = 30
evenly_divisible(1, 10, 3) ➞ 18
# 3 + 6 + 9 = 18'''

def inclusive(p, q, r):
    p = int(p)
    q = int(q)
    r = int(r)
    sum = 0
    for i in range(p, q+1):
        if i%r == 0:
            sum = sum + i
        if sum==0:
            continue
            
    if r>q:
        print(f"No number between {p} and {q} can be evenly divided by {r}")
    return sum

print(inclusive(1,10,2))
print(inclusive(1,10,3))
print(inclusive(1,10,20))


# In[42]:


'''Question 24:
Create a function that returns True if a given inequality expression is correct and
False otherwise.
Examples
correct_signs("3 < 7 < 11") ➞ True
correct_signs("13 > 44 > 33 > 1") ➞ False
correct_signs("1 < 2 < 6 < 9 > 3") ➞ True'''


def check(s):    #---> here s is nothing but a string.
    r=eval(s) #---> eval function evaluates the “String” like a python expression and returns the result as an integer.
    if r:
        return True
    else:
        return False 
 
print(check("3 < 7 < 11"))
print(check("13 > 44 > 33 > 1"))
print(check("1 < 2 < 6 < 9 > 3"))


# In[49]:


'''Question 25:
Create a function that replaces all the vowels in a string with a specified character.
Examples
replace_vowels("the aardvark", "#") ➞ "th# ##rdv#rk"
replace_vowels("minnie mouse", "?") ➞ "m?nn?? m??s?"
replace_vowels("shakespeare", "*") ➞ "sh*k*sp**r*"'''

def replaceVowelsWithK(test_str, K):
 
    # creating list of vowels
    vowels_list = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
 
    # creating empty list
    new_string = []
 
    # converting the given string to list
    string_list = list(test_str)
 
    # running 1st iteration for
    # comparing all the
    # characters of string with
    # the vowel characters
    for char in string_list:
 
        # running 2nd iteration for
        # comparing all the characters
        # of vowels with the string character
        for char2 in vowels_list:
 
            # comparing string character
            # and vowel character
            if char == char2:
 
                # if condition is true then adding
                # the specific character entered
                # by the user in the new list
                new_string.append(K)
                break
 
        # else adding the character
        else:
            new_string.append(char)
 
    # return the converted list into string
    return(''.join(new_string))
 
   
 
# Driver Code
# input string
input_str = "the aardvark"
 
# specified character
K = "#"
 
# printing input
print("Given Sting:", input_str)
print("Given Specified Character:", K)
print("After replacing vowels with the specified character:",
      replaceVowelsWithK(input_str, K))
        


# In[13]:


'''Question 26:
Write a function that calculates the factorial of a number recursively.
Examples
factorial(5) ➞ 120
factorial(3) ➞ 6
factorial(1) ➞ 1
factorial(0) ➞ 1'''

def fact(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n>1:
        factorial = (n * fact(n-1))
        return factorial
    

print(fact(5))
print(fact(3))
print(fact(1))
print(fact(0))


# In[21]:


'''Question 27:
Hamming distance is the number of characters that differ between two strings.
To illustrate:
String1: "abcbba"
String2: "abcbda"'''

def hammingDist(str1, str2):
    i = 0
    count = 0
 
    while(i < len(str1)):
        if(str1[i] != str2[i]):
            count += 1
        i += 1
    return count
 
# Driver code 
str1 = "geekspractice"
str2 = "nerdspractise"
 
# function call
print(hammingDist(str1, str2))


# In[31]:


'''Question 28:
Create a function that takes a list of non-negative integers and strings and return a new list
without the strings.
Examples
filter_list([1, 2, "a", "b"]) ➞ [1, 2]
filter_list([1, "a", "b", 0, 15]) ➞ [1, 0, 15]
filter_list([1, 2, "aasf", "1", "123", 123]) ➞ [1, 2, 123]
'''

def filter_list(l):
    list = []
    for i in l:
        if type(i) == int:
            list.append(i)
    return list
l1 = [1, 2, 'a', 'b']
l2 = [1, "a", "b", 0, 15]
l3 = [1, 2, "aasf", "1", "123", 123]
print(filter_list(l1))
print(filter_list(l2))
print(filter_list(l3))


# In[37]:


'''Question 29:
Print words of a string in reverse order.
'''

def wordReverse(str):
    i = len(str)-1
    start = end = i+1
    result = ''
 
    while i >= 0:
        if str[i] == ' ':
            start = i+1
            while start != end:
                result += str[start]
                start += 1
            result += ' '
            end = i
        i -= 1
    start = 0
    while start != end:
        result += str[start]
        start += 1
    return result

str = "Hello World"
print(wordReverse(str))


# In[42]:


'''Question 30:
The "Reverser" takes a string as input and returns that string in reverse order, with the
opposite case.
Examples
reverse("Hello World") ➞ "DLROw OLLEh"
reverse("ReVeRsE") ➞ "eSrEvEr"
reverse("Radar") ➞ "RADAr"'''
def reverse_for_loop(s):
    s1 = ''
    for c in s:
        s1 = c + s1   #---> appending chars in reverse order.
    return s1.swapcase()  #---> swaping letter case.

print(reverse_for_loop("Hello World"))
print(reverse_for_loop("ReVeRsE"))
print(reverse_for_loop("Radar"))


# In[49]:


'''Question 31:
You can assign variables from lists like this:
lst = [1, 2, 3, 4, 5, 6]
first = lst[0]
middle = lst[1:-1]
last = lst[-1]
print(first) ➞ outputs 1
print(middle) ➞ outputs [2, 3, 4, 5]
print(last) ➞ outputs 6

Your task is to unpack the list writeyourcodehere into three variables, being first,
middle, and last, with middle being everything in between the first and last element. Then
print all three variables.'''

list = [1, 2, 3, 4, 5, 6]
print(list[0])
print(list[1: (len(list) - 1)])  #---> or {print(list[1: -1])}
print(list[-1])


# In[22]:


'''Question 32:
Write a function that moves all elements of one type to the end of the list.
Examples
move_to_end([1, 3, 2, 4, 4, 1], 1) ➞ [3, 2, 4, 4, 1, 1]
# Move all the 1s to the end of the array.
move_to_end([7, 8, 9, 1, 2, 3, 4], 9) ➞ [7, 8, 1, 2, 3, 4, 9]
move_to_end{["a", "a", "a", "b"], "a"} ➞ ["b", "a", "a", "a"]
'''
# test_list = [1, 3, 2, 4, 4, 1]
def move_to_end(test_list, b):
    if type(b) == int:
        test_list.append(test_list.pop(test_list.index(1)))
        return test_list
    elif type(b) == str:
        test_list.append(test_list.pop(test_list.index(1)))
        return str(test_list)

print(move_to_end([1, 3, 2, 4, 4, 1], 1))
print(move_to_end([7, 8, 9, 1, 2, 3, 4], 9))
# print(move_to_end(["a", "a", "a", "b"], "a"))

    


# In[8]:


'''Question 33:
Create a function that takes a string and returns a string in which each character is repeated
once.
Examples
double_char("String") ➞ "SSttrriinngg"
double_char("Hello World!") ➞ "HHeelllloo WWoorrlldd!!"
double_char("1234!_ ") ➞ "11223344!!__ "
'''
def double_char(word):
    for i in word:
        print(f"{str(i) * 2}", end = '')
        
        
print(double_char("String"))
print(double_char("Hello World!"))
print(double_char("1234!_"))


# In[25]:


'''Question 34:
Create a function that reverses a boolean value and returns the string &quot;boolean expected&quot;
if another variable type is given.
Examples
reverse(True) ➞ False
reverse(False) ➞ True
reverse(0) ➞ "boolean expected"
reverse(None) ➞ "boolean expected"
'''
def reverse(input):
    if type(input) == bool:
        return not input
    else:
        return "boolean expected"
print(reverse(True))
print(reverse(False))
print(reverse(0))
print(reverse(None))


# In[29]:


'''Question 35:
Create a function that returns the thickness (in meters) of a piece of paper after folding it n
number of times. The paper starts off with a thickness of 0.5mm.
Examples
num_layers(1) ➞ "0.001m"
# Paper folded once is 1mm (equal to 0.001m)
num_layers(4) ➞ "0.008m"
# Paper folded 4 times is 8mm (equal to 0.008m)
num_layers(21) ➞ "1048.576m"
# Paper folded 21 times is 1048576mm (equal to 1048.576m)'''
# Formula ---> New thickness = [(0.5 * 2^n) * 0.001] meter

def num_layers(n):
    new_thickness = (0.5 * 2**n) * 0.001
    return new_thickness

print(num_layers(1))
print(num_layers(4))
print(num_layers(21))


# In[67]:


'''Question 36:
Create a function that takes a single string as argument and returns an ordered list containing
the indices of all capital letters in the string.
'''

def index_of_caps(string):
    res = [i for i, chr in enumerate(string) if chr.isupper()]
    return res
print(index_of_caps("eDaBiT"))
print(index_of_caps("eQuINoX"))
print(index_of_caps("determine"))
print(index_of_caps("STRIKE"))
print(index_of_caps("sUn"))


# In[70]:


'''Question 37:
Using list comprehensions, create a function that finds all even numbers from 1 to the given
number.
Examples
find_even_nums(8) ➞ [2, 4, 6, 8]
find_even_nums(4) ➞ [2, 4]
find_even_nums(2) ➞ [2]
'''
def find_even_nums(n):
    list = []
    for i in range(1, n+1):
        if i%2 == 0:
            list.append(i)
    return list
print(find_even_nums(8))
print(find_even_nums(4))
print(find_even_nums(2))


# In[3]:


'''Question 38:
Create a function that takes a list of strings and integers, and filters out the list so that it
returns a list of integers only.
'''

def filter_list(list):
    l = []
    for i in list:
        if type(i) == int:
            l.append(i)
        else:
            continue
    return l
print(filter_list([1, 2, 3, "a", "b", 4]))
print(filter_list(["A", 0, "Edabit", 1729, "Python", "1729"]))
print(filter_list(["Nothing", "here"]))


# In[18]:


list = [12, 23, 35, 47]
print(list[3])
print(list.index(35))


# In[3]:


'''Question 39:
Given a list of numbers, create a function which returns the list but with each element&#39;s
index in the list added to itself. This means you add 0 to the number at index 0, add 1 to the
number at index 1, etc...
Examples
add_indexes([0, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4]
add_indexes([1, 2, 3, 4, 5]) ➞ [1, 3, 5, 7, 9]
add_indexes([5, 4, 3, 2, 1]) ➞ [5, 5, 5, 5, 5]
'''
def add_indexes(list):
    l1 = []
    b = 0
    for i in list:
        l1.append(i+b)
        b += 1
    
    return l1

print(add_indexes([0, 0, 0, 0, 0]))
print(add_indexes([1, 2, 3, 4, 5]))
print(add_indexes([5, 4, 3, 2, 1]))


# In[4]:


'''Question 40:
Create a function that takes the height and radius of a cone as arguments and returns the
volume of the cone rounded to the nearest hundredth. See the resources tab for the formula.
Examples
cone_volume(3, 2) ➞ 12.57
cone_volume(15, 6) ➞ 565.49
cone_volume(18, 0) ➞ 0
'''
#Volume of right circular cone(V)---> (V=π*r^2*h/3)

from math import pi
def cone_volume(h, r):
    v = (pi*r**2*h)/3
    format_float = "{:.2f}".format(v)
    return format_float
print(cone_volume(3,2))
print(cone_volume(15,6))
print(cone_volume(18,0))
    


# In[5]:


'''Question 41:
This Triangular Number Sequence is generated from a pattern of dots that form a triangle.
The first 5 numbers of the sequence, or dots, are:
1, 3, 6, 10, 15
This means that the first triangle has just one dot, the second one has three dots, the third one
has 6 dots and so on.
Write a function that gives the number of dots with its corresponding triangle number of the
sequence.
Examples
triangle(1) ➞ 1
triangle(6) ➞ 21
triangle(215) ➞ 23220
'''

def triangle(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum
print(triangle(1))
print(triangle(6))
print(triangle(215))


# In[6]:


'''Question 42:
Create a function that takes a list of numbers between 1 and 10 (excluding one number) and
returns the missing number.
Examples
missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]) ➞ 5
missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]) ➞ 10
missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9]) ➞ 7
'''

def missing_num(list):
    for i in range(1, 11):
        if i not in list:
            missing_number = i
    return missing_number
print(missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]))
print(missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]))
print(missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9]))


# In[7]:


'''Question 43:
Write a function that takes a list and a number as arguments. Add the number to the end of
the list, then remove the first element of the list. The function should then return the updated
list.
Examples
next_in_line([5, 6, 7, 8, 9], 1) ➞ [6, 7, 8, 9, 1]
next_in_line([7, 6, 3, 23, 17], 10) ➞ [6, 3, 23, 17, 10]
next_in_line([1, 10, 20, 42 ], 6) ➞ [10, 20, 42, 6]
next_in_line([], 6) ➞ "No list has been selected"
'''

def next_in_line(list, n):
    if len(list) != 0:
        list.pop(0)
        a = len(list)
        list.insert(a, n)
        return list
    elif len(list) == 0:
        return ("No list has been selected")

print(next_in_line([5, 6, 7, 8, 9], 1))
print(next_in_line([7, 6, 3, 23, 17], 10))
print(next_in_line([1, 10, 20, 42], 6))
print(next_in_line([], 6))


# In[8]:


'''Question 44:
Create the function that takes a list of dictionaries and returns the sum of people's budgets.
'''

def get_budgets(list):
    sum = 0
    for d in list:
        a = d.get("budget")
        sum += a
    return sum
print(get_budgets([{ "name": "John", "age": 21, "budget" : 23000 },
               { "name": "Steve", "age": 32, "budget" : 40000 },
               { "name": "Martin", "age": 16, "budget" : 2700 }]))
print(get_budgets([
                { "name": "John", "age": 21, "budget": 29000 },
                { "name": "Steve", "age": 32, "budget": 32000 },
                { "name": "Martin", "age": 16, "budget": 1600 }]))


# In[9]:


'''Question 45:
Create a function that takes a string and returns 
a string with its letters in alphabetical order.
'''
# ---> By using sorted() with join().
def alphabet_soup(str):
    return ''.join(sorted(str))

print(alphabet_soup("hello"))
print(alphabet_soup("edabit"))
print(alphabet_soup("hacker"))
print(alphabet_soup("geek"))
print(alphabet_soup("javascript"))


# In[10]:


'''Question 46:
Create a function that takes three parameters where:
 x is the start of the range (inclusive).
 y is the end of the range (inclusive).
 n is the divisor to be checked against.
Return an ordered list with numbers in the range that are divisible by the third parameter n.
Return an empty list if there are no numbers that are divisible by n.
Examples
list_operation(1, 10, 3) ➞ [3, 6, 9]
list_operation(7, 9, 2) ➞ [8]
list_operation(15, 20, 7) ➞ []
'''

def list_operation(x, y, n):
    list = []
    for i in range(x,y):
        if i%n == 0:
            list.append(i)
    return list
print(list_operation(1, 10,3))
print(list_operation(7, 9, 2))
print(list_operation(15, 20, 7))


# In[18]:


''' Question 47:
Create a function that takes in two lists and returns True if the second list follows the first list
by one element, and False otherwise. In other words, determine if the second list is the first
list shifted to the right by 1.
Examples
simon_says([1, 2], [5, 1]) ➞ True
simon_says([1, 2], [5, 5]) ➞ False
simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]) ➞ True
simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3]) ➞ False
Notes
 Both input lists will be of the same length, and will have a minimum length of 2.
 The values of the 0-indexed element in the second list and the n-1th indexed element
in the first list do not matter.
'''

l1 = [1, 2, 3, 4]
l2 = [5, 1, 2, 3]
a = True
for i in range(0, len(l1)):
    if l1[i] != l2[i+1]:
        a = False
        print(a)
        break
****************************************CORRECT IT...


# In[36]:


'''Question 48:
A group of friends have decided to start a secret society. The name will be the first letter of
each of their names, sorted in alphabetical order.
Create a function that takes in a list of names and returns the name of the secret society.
'''

def society_name(list):
    l1 = []
    for i in list:
        l1.append(i[0])
    string = ''.join(sorted(l1))
    return string
print(society_name(["Adam", "Sarah", "Malcolm"]))
print(society_name(["Harry", "Newt", "Luna", "Cho"]))
print(society_name(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"]))


# In[49]:


'''Question 49:
An isogram is a word that has no duplicate letters. Create a function that takes a string and
returns either True or False depending on whether or not it's an "isogram".
Notes
 Ignore letter case (should not be case sensitive).
 All test cases contain valid one word strings.
'''

def is_isogram(word):
 
    # Convert the word or sentence in lower case letters.
    clean_word = word.lower()
 
    # Make an empty list to append unique letters
    letter_list = []
 
    for letter in clean_word:
 
        # If letter is an alphabet then only check
        if letter.isalpha():
            if letter in letter_list:
                return False
            letter_list.append(letter)
 
    return True

print(is_isogram("Algorism"))
print(is_isogram("PasSWord"))
print(is_isogram("Consecutive"))


# In[52]:


'''Question 50:
Create a function that takes a string and returns True or False, depending on whether the
characters are in order or not.
'''
def is_in_alphabetical_Order(word):
    for i in range(len(word) - 1):
        if word[i] > word[i + 1]:
            return False
    return True
print(is_in_alphabetical_Order("abc"))
print(is_in_alphabetical_Order("edabit"))
print(is_in_alphabetical_Order("123"))
print(is_in_alphabetical_Order("xyzz"))

************************Understand it!......


# In[ ]:




