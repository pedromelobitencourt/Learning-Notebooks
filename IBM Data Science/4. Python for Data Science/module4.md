# Reading and Writing Files

## Reading Files with Open

We use Python's `open` function to get a **file object**

You should always close the file after you are done with it

```python
file = open('filename.txt', 'r')
```

The first argument is the file path and the second argument is the mode. The mode can be:

- `'r'` - read
- `'w'` - write
- `'a'` - append
- `'r+'` - read and write
- `'b'` - binary
- `'t'` - text
- `'x'` - create
- `'+'` - read and write
- `'U'` - universal newline
- `'rb'` - read binary
- `'wb'` - write binary
- `'ab'` - append binary
- `'r+b'` - read and write binary
- `'x+b'` - create binary

## Getting the name of the file

We can get the name of the file with the `name` attribute

```python
file = open('filename.txt', 'r')
print(file.name)
file.close()
```

## Reading Files with Read

We can read the contents of a file with the `read` method

```python
file = open('filename.txt', 'r')
content = file.read()
print(content)
file.close()
```

## Reading Files with Readline

We can read the contents of a file line by line with the `readline` method

```python
file = open('filename.txt', 'r')
line = file.readline()
print(line)
file.close()
```

## Reading Files with Readlines

We can read the contents of a file line by line with the `readlines` method

```python
file = open('filename.txt', 'r')
lines = file.readlines()
print(lines)
file.close()
```

## Reading files with With Open

We can use a `with` statement to automatically close the file

```python
with open('filename.txt', 'r') as file1:
    file_content = file1.read()
    print(file_content)

print(file1.closed)
print(file_content)
```

## Writing Files with Open

We can write to a file with the `write` method

```python
file = open('filename.txt', 'w')
file.write('Hello World')
file.close()
```

If you have the same file in the current directory, it will be overwritten

## With Open for Writing

We can use a `with` statement to automatically close the file

```python
with open('filename.txt', 'w') as file1:
    file1.write('Hello World')

print(file1.closed)
```

## Appending Files with Open

We can append to a file with the `write` method

```python
file = open('filename.txt', 'a')
file.write('Hello World')
file.close()
```

# Pandas

Pandas is a popular library for data analysis

```python
import pandas as pd
```

## Loading Data

### Dataframe

Dataframes are the primary data structure in Pandas

A dataframe is comprised of rows and columns

```python
df = pd.DataFrame()
```

### CSV file

```python
df = pd.read_csv('filename.csv')
```

### Excel file

```python
df = pd.read_excel('filename.xlsx')
```

### JSON file

```python
df = pd.read_json('filename.json')
```

### Methods

* **head()** - first 5 rows
* **tail()** - last 5 rows

### Create a Dataframe out of a dictionary

The keys are the column names and the values are the data

```python
data = {
    'Name': ['Tom', 'Jerry'],
    'Age': [20, 21]
}

df = pd.DataFrame(data)
```

### Create a Dataframe out of an existing Dataframe

```python
df2 = df[['Name', 'Age']]
```

### Replace the index

```python
df.index = ['a', 'b']
```

### Accessing Data

```python
df['Name']
df['Name'][0]
df['Name'][0:2]
```

We can also use the `iloc` method

```python
df.iloc[0]
df.iloc[0, 0]
df.iloc[0:2, 0]
```

You can use the name of the columns

```python
df.loc[0, 'Name']
```

## Working with and Saving Data

### Working with Data

**unique()** - get unique values from a column

```python
df['Name'].unique()
```

**value_counts()** - get the count of unique values

```python
df['Name'].value_counts()
```

**sort_values()** - sort the values

```python
df.sort_values('Name')
```

**isnull()** - check for missing values

```python
df.isnull()
```

**Applying inequalities**

```python
df['Age'] > 20 # returns an index list of Boolean values
```

**Getting the rows that satisfy the condition**

```python
new_df = df[df['Age'] > 20]
```

### Saving Data

**to_csv()** - save to a CSV file

```python
df.to_csv('new_file.csv')
```

**to_excel()** - save to an Excel file

```python
df.to_excel('new_file.xlsx')
```

**to_json()** - save to a JSON file

```python
df.to_json('new_file.json')
```