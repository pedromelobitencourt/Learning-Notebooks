# Conditions and Branching

## Comparison Operators

Comparison operations compare some value or operand and, based on a condition, they produce a Boolean

When comparing two values you can use these operators:

- equal: `==`
- not equal: `!=`
- greater than: `>`
- less than: `<`
- greater than or equal to: `>=`
- less than or equal to: `<=`

### Examples

```python
# Equal
print(1 == 1) # True
print(1 == 2) # False

# Not equal
print(1 != 1) # False
print(1 != 2) # True

# Greater than
print(1 > 1) # False
print(1 > 2) # False

# Less than
print(1 < 1) # False
print(1 < 2) # True

# Greater than or equal to
print(1 >= 1) # True
print(1 >= 2) # False

# Less than or equal to
print(1 <= 1) # True
print(1 <= 2) # True
```

## Branching

Branching allows us to run different statements for different inputs

It is helpful to think of an `if` statement as a locked room, if the statement is `True` we can enter the room and your program will run some predefined tasks, but if the statement is `False` the program will ignore the task or do some other task

### If statement

```python
age = 19

if age > 18:
    print("You can enter")
```

### If-else statement

```python
age = 19

if age > 18:
    print("You can enter")
else:
    print("You can't enter")
```

### If-elif-else statement

```python
age = 19

if age > 18:
    print("You can enter")
elif age == 18:
    print("You can enter next year")
else:
    print("You can't enter")
```

## Logical Operators

Logical operators allow you to combine or modify conditions

- `and`: `True` if both the operands are `True`

- `or`: `True` if either of the operands is `True`

- `not`: `True` if the operand is `False`

### Examples

```python
# and
print(True and True) # True
print(True and False) # False

# or
print(True or True) # True
print(True or False) # True

# not
print(not True) # False
print(not False) # True
```

# Loops

## Range Function

The `range` function allows you to generate a sequence of numbers

If the input is a single number, let's say `n`, the function generates a sequence of numbers starting from `0` to `n-1`

```python
print(range(5)) # range(0, 5): 0, 1, 2, 3, 4
```

If the input is two numbers, let's say `m` and `n`, the function generates a sequence of numbers starting from `m` to `n-1`

```python
print(range(2, 5)) # range(2, 5): 2, 3, 4
```

## For Loop

The `for` loop is used to iterate over a sequence (list, tuple, string) or other iterable objects

```python
for i in range(5):
    print(i)
```

### Example

```python
dates = [1982, 1980, 1973]

for year in dates:
    print(year)
```

### Enumerate

The `enumerate` function adds a counter (starting at 0) to an iterable

```python
for i, year in enumerate(dates):
    print(i, year)
```

## While Loop

The `while` loop is used to execute a block of statements repeatedly until a given condition is `False`

```python
count = 0

while count < 5:
    print(count)
    count += 1
```


# Functions

A function is a block of organized, reusable code that is used to perform a single, related action

Functions provide better modularity for your application and a high degree of code reusing

Functions take some input, then produce some output or change the state of some object

## Defining a Function

You can define functions to provide the required functionality

A function is defined by using the `def` keyword, followed by a function name, a signature within parentheses `()`, and a colon `:`

The function body can contain a `return` statement

```python
def add(a, b):
    return a + b
```

## Calling a Function

Once we have defined a function, we can call it from another function, program, or even the Python prompt

To call a function, use the function name followed by `()`

```python
ans = add(1, 2) # 3
```

## Default Arguments

You can set a default value for arguments in your function

```python
def add(a, b=2):
    return a + b

print(add(1)) # 3
print(add(1, 3)) # 4
```

## Python Built-in Functions

Python comes with many built-in functions that are readily available to use

```python
print(abs(-1)) # 1
print(type(1)) # <class 'int'>
print(len([1, 2, 3])) # 3
print(sum([1, 2, 3])) # 6
```

### Sorted

The `sorted` function returns a new sorted list from the elements of any iterable

**It does not modify the original list**

```python
List = [3, 1, 2]
sorted_list = sorted(List) # [1, 2, 3]
```

### Sort

The `sort` method modifies the original list

```python
List = [3, 1, 2]
List.sort()
print(List) # [1, 2, 3]
```

## User-defined Functions

You can define your own functions in Python

If your function does not have a `return` statement, it will return `None`

```python
def is_even(num):
    return num % 2 == 0

print(is_even(4)) # True
print(is_even(5)) # False
```

### Adding Docstrings

You can add a docstring to your function to describe what it does

You can use the `help` function to read the docstring

```python
def is_even(num):
    """
    Check if a number is even
    
    Args:
        num: int, number to check
        
    Returns:
        bool, True if the number is even, False otherwise
    """
    return num % 2 == 0
```

### Pass keyword

The `pass` keyword is used to execute nothing

The `pass` is also useful in places where your code will eventually go, but has not been written yet

```python
def function(args):
    pass # later
```

### Collecting arguments

You can collect arguments in a tuple using the `*` operator

```python
def add(*args):
    return sum(args)

print(add(1, 2, 3)) # 6, args is (1, 2, 3)
```

## Lambda Functions

A lambda function is a small anonymous function

A lambda function can take any number of arguments, but can only have one expression

```python
add = lambda a, b: a + b
print(add(1, 2)) # 3
```

# Exception Handling

