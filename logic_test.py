"""
1. Code a program (in python) that displays the numbers from 1 to 100 on the
screen, substituting the multiples of 3 for the word "fizz", the multiples of 5 for
"buzz" and the multiples of both, that is, the multiples of 3 and 5, by the word
"fizz buzz".
"""
from logic import fizzbuzz

def test_fizzbuzz(capfd):
    fizzbuzz()
    out, err = capfd.readouterr()
    result = out.split('\n')
    for index, value in enumerate(result):
        num = index + 1
        if not value:
            continue
        if num % 15 == 0:
            assert value == "fizz buzz"
        elif num % 3 == 0:
            assert value == "fizz"
        elif num % 5 == 0:
            assert value == "buzz"
        else:
            assert value == str(num)

"""
2. In mathematics, the Fibonacci sequence or serie is the following infinite sequence
of natural numbers: 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597 ...
where f (0) = 0, f (1) = 1 and f (n) = f (n-1) + f (n-2).
Code a program (in python) that solves for any number in the Fibonacci series.
"""
from logic import fibonacci

def test_fibonacci():
    assert fibonacci("123") == -1
    assert fibonacci(-2) == -1
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(10) == 55
    assert fibonacci(50) == 12586269025
    assert fibonacci(100) == 354224848179261915075

"""
3. Given an input text, Code a program (in python) that displays the number of
repetitions of each word.
Sample text: "Hi how are things? How are you? Are you a developer? I am also a developer"
"""
from logic import countWords

def test_countWord():
    count = countWords("Hi how are things? How are you? Are you a developer? I am also a developer")
    assert count.get("how", 0) == 2
    assert count.get("are", 0) == 3
    assert count.get("hello", 0) == 0