#message = 'Hello World!'
#print(message)

'''
if True == True:
    print('True')
else:
    print('False')
'''
'''
#Basic String Operations
name = 'SOUMAHORO Sahi Ibrahim'
#print(name[len(name) - 1])
#print(len(name))
mot1 = 'Hello'
mot2 = ' World'
print(mot1 + mot2)
'''
#String Slicing and Indexing
'''
text = "Python Programming"
print(text[0:6])
print(text[-6:])
print(text[12:])
print(text[::-1])
print(text[::-1])
'''

# String Methods and Functions
exo = " i love python programming "
#print(exo.strip())
#print(exo.title())
#print(exo.count("o"))
#print(exo.isalnum())
#print(exo.isalpha())

# String Formatting and f-Strings
'''
name = 'John'
age = 25
#print("My name is {} and I am {} years old.".format(name, age))
print(f" My name is {name} and I am {age} years old")
'''

#String Manipulation Challenges
'''
srt1 = 'Coding in Python is fun'
print(srt1.replace('fun', 'awesome'))
print(srt1.find('Python'))
print(srt1.upper())
'''

#Write a program that counts how many vowels are in a given string.
'''
Algorithm CountVowels
1. Start
2. Read a sentence
3. Set count ← 0
4. For each character in the sentence:
      If the character is 'a', 'e', 'i', 'o', or 'u'
         count ← count + 1
5. Display count
6. End
'''
str2 = 'Coding in Python is fun'
count = 0
for character in str2.lower():
   if character in 'aeiou':
       count += 1
print(count)

'''
#Method 1: Using count()
sentence = input("Enter a sentence: ")
count = (
    sentence.lower().count('a') +
    sentence.lower().count('e') +
    sentence.lower().count('i') +
    sentence.lower().count('o') +
    sentence.lower().count('u')
)
print("Number of vowels:", count)
'''

'''
Method 2: Using a for loop
sentence = input("Enter a sentence: ")

count = 0

for letter in sentence:
    if letter.lower() in "aeiou":
        count += 1

print("Number of vowels:", count)
'''

'''
Method 3: Using a while loop
sentence = input("Enter a sentence: ")

count = 0
i = 0

while i < len(sentence):
    if sentence[i].lower() in "aeiou":
        count += 1
    i += 1

print("Number of vowels:", count)
'''

'''
Method 4: Using a function
def count_vowels(sentence):
    count = 0

    for letter in sentence.lower():
        if letter in "aeiou":
            count += 1

    return count

sentence = input("Enter a sentence: ")
print("Number of vowels:", count_vowels(sentence))
'''

'''
Method 5: Using sum()
sentence = input("Enter a sentence: ")

count = sum(1 for letter in sentence.lower() if letter in "aeiou")

print("Number of vowels:", count)
produces 1 each time a vowel is found, and sum() adds them.
'''

'''
Method 6: Count each vowel separately
sentence = input("Enter a sentence: ").lower()

a = sentence.count('a')
e = sentence.count('e')
i = sentence.count('i')
o = sentence.count('o')
u = sentence.count('u')

print("a:", a)
print("e:", e)
print("i:", i)
print("o:", o)
print("u:", u)

print("Total vowels:", a + e + i + o + u)
'''

'''
Algorithm CheckPalindrome
1. Start
2. Read string S
3. Reverse S and store it in R
4. If S = R then
      Display "Palindrome"
   Else
      Display "Not a palindrome"
5. End
'''
#Take a user input string and check if it is a palindrome (same forwards and backwards).
text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

'''
Method 3: Without using reverse
text = input("Enter a string: ")

is_palindrome = True

for i in range(len(text) // 2):
    if text[i] != text[len(text) - 1 - i]:
        is_palindrome = False
        break

if is_palindrome:
    print("Palindrome")
else:
    print("Not a palindrome")
 
'''

#Factorial Ask the user for an integer n and calculate its factorial using a while loop. Example: 5! = 120.
#Fibonacci Sequence Print the first 10 numbers of the Fibonacci sequence using a loop.