# Notes from the workshop
During this section Michael used a python REPL

You can start a REPL with `python` in a terminal

## variables
`age = 1`

## Basic math
```
7 // 2 # 3
7 / 2 # 3.5
import math
math.pi # 3.14..
```

## f-strings
```
age = 1
f"Hi, my age is {age}" # 'Hi my age is 1'
```

 ## Booleans
`True` and `False` (capital)

## None
`None` is the equivalent of `undefined` or `null` in JavaScript, means no value

## Comparison operators
`==` compares value

`is` compares reference

`1 == 1` true

`1 is 1` true

`a = None`

`b = None`

`a is b` true, only one None

## Strings
String methods, `dir(str)`

`s = 'Hi There'`

`s.find(' ')` returns index 2

`s[2]` returns `' '`

`s[0:2:1]` same results `s[start:stop:step]`

^Indexing for anything in python that's an iterable

`s[::-1]` reverse string

## lists
`l = [1, 2, 3, 4, 5, 6]`

`l[::3]` returns `[1, 4, 7]`, doesn't mutate original string

`l += [7]` mutates l and appends 7

`l.sort()` sorts in place

`sorted(l)` returns new list

## classes
```
class Chest:
  pass
```
`pass`- skips line
`c = Chest()`

## tuples
`(1, 2, 3)`

Cannot be mutated or changed, Python loves tuples!

## functions
```
def myfunc():
  return 3
```

`myfunc()` returns 3

```
def myfunc2():
  return 3, 's'
```

`myfunc2()` returns `(3, 's')`

returning from a function

`a = myfunc()`

`a` equals 3

`a, b = myfunc2()`

`a` equals 3

`b` equals 's'

## unpacking multiple values
`row = (1, "Michael", 28, 1293812)`

`id, data = row` error

`id, *data = row`

id is 1, data is ['Michael', 28, 1293812]`

`*data, hours = row` hours is 1293812

`id, *data, hours = row` id is 1, hours is 1293812

## sets
denoted by `{}`

`s = {1, 78, 3}`

`s` is {1, 3, 78}

dedupe a list, `list(set([2,2,3])` returns `[2,3]`

add to a set

`s.add(9)`

s is `{1, 3, 9, 78}`

## dictionary (like objects in JS)
uses curly braces as well, but with key:value pairs

`d = { "age": 28, "name": "Michael" }`

`d.keys()` age, name

`d.values()` 28, Michael

`d.items()` list of items

`d["name"]` returns Michael

## loops
```
l = [2, 5, 7]
for n in l:
  print(n)
```
prints 2, 5, 7 on separate lines

loop backwards

`for n in l[::-1]:`

or 

`for n in reversed(l):`

loop through dictionary

```
for key in d:`
  print(key, d[key])
```
better
```
for key, val in d.items():
  print(key, val)
```

while loops

```
i = 0
while i < 10:
  print(i)
  i += 1
```
prints 0 - 9 on new lines

## ranges (generator)
`l = range(10)`

`l` is `range(0, 10)

```
for i in range(10):
  print(i)
```

prints 0 - 9

```
for i in range(5, 10):
  print(i)
```

prints 5 - 9

```
for i in range(0, 10, 2):
  print(i)
```

prints evens

## getting length
built-in length function `len()` gives you length of str, dict, set, list, etc

loop through row

`for i in range(len(row)): print(row[i])`

`for i, val in enumerate(row): print(i, val)`

backwards

`for i, val in reversed(list(enumerate(row))): print(i, val)` prints reversed index, val

## python built-in functions 
[https://docs.python.org/3/library/functions.html](https://docs.python.org/3/library/functions.html)

### Notes
don't use `[]` in default arguments!

`def doStuff(n1 = 1, n2 = []):` <-bad!

keyword args, you can pass arguments out of order:

```
def printNums(n1, n2):
   print(f"n1 is {n1}, n2 is {n2}")

printNums(n2=1, n1=3)
```

truthy/falsy values

`argparse` stdlib for parsing command line arguments

`_` means ignore this variable

everything in python is an object/first class citizen

first class citizen means can be supplied as parameter to a function

`l.append.__doc__` # prints description

`help()` prints help file

`lamba x: 1 + x` creates an anonymous function that returns x + 1
