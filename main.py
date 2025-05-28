import * from app.py

print("Hello world")
print("red")
print("google")
print("hell")

def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]

def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
