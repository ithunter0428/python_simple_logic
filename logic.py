"""
1. Code a program (in python) that displays the numbers from 1 to 100 on the
screen, substituting the multiples of 3 for the word "fizz", the multiples of 5 for
"buzz" and the multiples of both, that is, the multiples of 3 and 5, by the word
"fizz buzz".
"""
def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print("fizz buzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

"""
2. In mathematics, the Fibonacci sequence or serie is the following infinite sequence
of natural numbers: 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597 ...
where f (0) = 0, f (1) = 1 and f (n) = f (n-1) + f (n-2).
Code a program (in python) that solves for any number in the Fibonacci series.
"""

def fibonacci(number):
    if not isinstance(number, int) or number < 0:
        return -1
    elif number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(number):
            c = a + b
            a, b = b, c
        return a

"""
3. Given an input text, Code a program (in python) that displays the number of
repetitions of each word.
Sample text: "Hi how are things? How are you? Are you a developer? I am also a developer"
"""
import re

def countWords(str):
    words = re.findall(r'\w+', str)
    result = {}
    for word in words:
        word = word.lower()
        result[word] = result.get(word, 0) + 1
    return result

print(countWords("Hi how are things? How are you? Are you a developer? I am also a developer"))