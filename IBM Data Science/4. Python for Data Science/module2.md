# Lists and Tuples

They are compound data types

## Tuples

* They are **ordered sequences**

* Tuples are written as comma-separated elements within parentheses

```
Ratings = (1, 7, 2, 3, 4)
```

All types can be contained in the same tuple

```
tuple1 = ('disco', 1, 1.2)
type(tuple1) # tuple
```

* Each element of a tuple can be accessed by an index

```
tuple1 = ('disco', 1, 1.2)
tuple1[0] # 'disco'
tuple1[1] # 1
tuple1[2] # 1.2

tuple1[-3] # 'disco'
tuple1[-2] # 1
tuple1[-1] # 1.2
```

### Concatenate

```
tuple2 = tuple1 + ("hard rock", 10)
tuple2 # ('disco', 1, 1.2, 'hard rock', 10)
```

### Slicing

```
tuple2[0:3] # ('disco', 1, 1.2)
```

* Tuples are immutable, that is, we cannot change them

```
Ratings = (1, 8, 5, 3, 4)
RatingsSorted = sorted(Ratings) # (1, 3, 4, 5, 8)
```


## Lists

* They are an ordered sequence

* Lists are mutable

* They can contain any data type inside them

* Each element can be accessed by an index

* We can concatenate lists

```
L = [1, 3, 'hi']
L1 = L + [9, 'hello'] # [1, 3, 'hi', 9, 'hello']
```

### Extend

* Add a new list to the current list (without creating a new one)

```
L = [1, 3, 'hi']
L.extend('rock', 8) # L = [1, 3, 'hi', 'rock', 8]
```

### Append

* Add only an element

```
L = [1, 3, 'hi']
L.append(['rock', 8]) # L = [1, 3, 'hi', ['rock', 8]]
```

### del

```
L = [1, 3, 'hi']
del(L[2]) # L = [1, 3]
```


### Aliasing

```
A = [1, 3, 'hi']
B = A
```

Both lists, *A* and *B* are referencing the same *object*

```
B[0] = 2
A # [2, 3, 'hi']
```

### Clone lists

* Now if you change a list, the other one will not change as well

```
A = [1, 3, 'hi']
B = A[:]
```


# Dictionaries

* They are a type of collection in Python

In Lists or Tuples, the indexes were like the addresses of the elements

* Dictionaries have **keys** and **values** associated to these *keys*

* The keys can be any type

* They are denoted with curly brackets

* The keys must be **immutable** and **unique**

* The values can be **mutable**, immutable, **duplicates** or unique


```
DICT = {
    "Thriller": 1982, "Back in Black": 1980,
    "The Dark Side of the Moon": 1973,
    "The Bodyguard": 1992
}

DICT["Thriller"] # 1982
```

### Add a new value

```
DICT["Graduation"] = 2007
```

### Delete

```
del(DICT["Thriller"])
```

### Verify if an element is in the dictionary

```
"The Bodyguard" in DICT # True
"Starboy" in DICT # False
```

### List all keys

```
DICT.keys()
```

### List all values

```
DICT.values()
```


# Sets

* They are a type of **unordered** collection in Python
* They have only unique elements
* To define a Set, you use curly brackets

```python
Set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
```

In the example above, there are duplicate elements, but the Set will only contain unique elements

## Convert a list to a Set (Type Casting)

You can convert a list to a set using the function **set**

```python
album_list = ["Michael Jackson", "Thriller", 1982, "00:42:19", "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)
```

## Add an element to a Set

```python
album_set.add("Jazz")
```

## Remove an element from a Set

```python
album_set.remove("Jazz")
```

## Verify if an element is in the Set

```python
"Jazz" in album_set # False
```

## Find the intersection of two sets

Intersection is the common elements between two sets

```python
set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
set2 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco", "jazz", "blues"}
intersection = set1 & set2
```

## Find the union of two sets

Union is all elements from both sets

```python
union = set1.union(set2)
```

## Find if a set is a subset of another set

Subset is when all elements of the first set are in the second set

```python
set1.issubset(set2)
```

## Find if a set is a superset of another set

A superset is a set that contains all the elements of another set

```python
set1.issuperset(set2)
```

## Find the difference between two sets

Difference is the elements that are in the first set but not in the second set

```python
set1.difference(set2)
```

## Update

Add elements from another iterable to the current set

```python
set1.update(["jazz", "blues"])
```

## Pop

Remove an arbitrary element from the set

```python
arbitrary_element = set1.pop()
```

## Copy

Create a shallow copy of the set

```python
set1_copy = set1.copy()
```