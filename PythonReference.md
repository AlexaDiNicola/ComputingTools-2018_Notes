## Contents:

- [Background information](#background-information)
	- [Glossary]
- [Basic Python commands](#basic-shell-commands)
- [Data and data types](#data-and-data-types)
	- [Variables](#variables)
	- [Arithmetic](#arithmetic)
	- [Working with arrays](#working-with-arrays)
- [Doing Things basics](#doing-things-basics)
	- [Functions](#functions)
	- [Libraries](#libraries)
- [Visualization](#visualization)
	- [matplotlib](#matplotlib)
- [Functions by library](#functions-by-library)

	
----

## Background information

“The purpose of computing is insight, not numbers."  --Richard Hamming

- Python interpreters:
	- ``python``:
	- ``ipython``:
	- ``jupyter lab``:

### Glossary

- **array:** 
- argument:
- **element:** 
- **floating point:** 
- function: 
- **integer:** 
- **library:**
- **members:** AKA attributes. Metadata about a variable. For example, the NumPy array 
   ``data`` has members including ``data.dtype``, ``data.shape``
- **string:** 
- **shape:** (of an array) dimensions.
- **slice:** a subset of elements or characters from a list/array or string respectively.
  Usually described in colon notation: `0:4` is the slice from elements 0 through 3, i.e.
  up to but not including 4.
- **variable:** a name for a value, a pointer to data.


----

## Basic Python commands

- ``#``: Everything in a line after the octothorpe is a comment.
- ``?command``: get help on ``command``
	- ``help(command)``: get help on ``command``

----

## Data and data types

### Variables
"A variable is analogous to a sticky note with a name written on it."  (Software Carpentry)

- ``%whos``: display a table of all variables currently set.
- ``weight_kg = 60``: set ``weight_kg`` to 60. No need to declare a variable ahead of time.
	- Varnames can:
		- include alphanumerics & underscores
	- Varnames CANNOT:
		- include dots
		- start with a digit
	- Varnames are case sensitive.
- ``print(weight_kg)``: displays the value of ``weight_kg``.
	- ``print(weight_kg, weight_in_kilos)``: displays the value of ``weight_kg`` and then 
	   of ``weight_in_kilos``, with no separator.
	- ``print("weight in pounds: ", weight_kg * 2.2)``: You can do math and specify values
	   within a ``print()`` command.

### Data Types

- Numbers are stored as 64 bits, so the biggest **integer** we can easily store is 2^^64^^-1.
	- If you're storing a **negative number,** though, you use 1 bit for the sign and 63 for
	   the number... and the computer needs to know that that one bit is different
	- **Floating-point values** are stored effectively in scientific notation: one bit for 
	   the sign, some number (11?) for the exponent, the rest (52?) for the base value.
- So, 4 basic data types: integers (``int``), floating point numbers (``float``), strings 
   (``str``), & booleans (``bool``).
    - ``varname 60``: ``varname`` is an int, value 60 .
	- ``varname 60.0``: ``varname`` is a float, value 60.0 . NB: *Never test for exact equality of floats.* It won't work -- rounding error is tiny, but omnipresent.
	- ``varname "sixty"``: ``varname`` is a string, value "sixty".
	- ``varname True``: it's a bool, value ``True``. (``True``/``False`` must be in title case.)
	- ``varname None``: it's empty.
- ``type(weight)``: returns the data type for `weight`. For arrays, will only return the 
   array itself, not its elements.
- To convert between types, use the type abbreviation as a function:
	- `float(x)`: converts `x` to a floating-point number
	- `int(x)`: converts `x` to an integer by truncating at the decimal place
	- `bool(x)`: converts `x` to a boolean (0 or `None` is False, anything else is True)
- Converting numbers into strings: `"%s" % (5)` converts "5" to a string, then returns it.
	- `'%s %s hello %5' % (5, 5.8, "5")` returns the string "5 5.8 hello 5".
	- `'%d %d %d world' % (5, 5.8, int("51"))` returns "5 5 51 world" (`%d%` converts to a "digit" i.e. integer)

#### Storing multiple elements

- `[10, 20]` is a list of 2. Lists are mutable.
	- `(10, 20)` is a tuple of 2. Tuples are immutable.
	- A list of lists is not the same as a `numpy` array.
	- Lists can contain multiple data types: `a = [4, "Svitz", [0, 1, 2]]`
- To refer to one element of a list: (say `a = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12`)
	- `a[0]` returns 3, `a[1]` returns 4, etc.
	- `a[1:4]` returns [4, 5, 6] (elements 1 to 4, *not including element 4*)
	- `a[1:9:3]` returns [4, 7, 10] (every third element between 1 and 9)
- Modifying lists in place:
	- (As noted under Mutability below, be careful with this.)
	- `odds.append(11)`: add the value 11 to the end of list `odds`
	- `del odds[0]`: delete the first element of `odds`
	- `odds.reverse()`: reverse the order of elements in `odds`
- Modifying a list of lists:
	- `a = [  [1,2,3,4,5],  [6,7,8,9,10],  [11,12,13,14,15,16,17,18]  ]`. To return 9, 
	   you'll need two sets of brackets (two indices): `a[1][3]`.
- Mutability: Lists are mutable because you can edit just one element of a list. Strings 
  are immutable because you can't edit just one character of a string -- you have to 
  replace the whole string.
	- `guy = "Darwin" ; dude = guy ; print(dude)"` returns "Darwin". Because strings are
	   immutable, setting `guy = "Pasteur"` won't affect the value of `dude`.
	- If you set a variable to another MUTABLE variable, they're now just pointers that 
	   refer to the same place. `people = ["Darwin", "Pasteur"] ; folks = people; print(folks)` 
	   returns "["Darwin", "Pasteur"], and *if you edit* `people`, `folks` *will also change.*
	- To copy a list instead, use `folks = list(people)`.
	- The `copy` library has some useful operations for dealing with this.
- 

`taxon = "Ursus arctos horribilis"`
`taxon.split(" ")` returns ["Ursus", "arctos", "horribilis"]
`taxon. [???]  ` returns... **what?**
`taxon.strip()` removes leading & trailing newlines, tabs, & spaces

### Arithmetic

- Basic arithmetic operations are very simple: `` 3 + 5 * 4`` returns ``20``.
- Some array operations with ``numpy``:
	- ``numpy.mean(data, axis=0)``: returns a vector of the averages of each row in ``data``
	- ``numpy.mean(data, axis=1)``: returns a vector of the averages of each column in ``data``

### Working with arrays

- ``data[0, 0]``: first (top-left) value in an array. (Python is zero-indexed because it's
   part of the C family, like C++ and Perl.)
	- The first value is the row (Y-coord), the second value is the column (X-coord). They
	   work like matrices, not Cartesian coordinates.
	- ``data[0:4, 1:10]``: rows 0-3 (the 1st-3rd) of columns 1-9 (the 2nd-10th). Note that
	   this is *up to, but not including* row 4 and column 10.
	- ``data[:3, 10:]``: rows up to 3 (i.e. 0-2) of all columns after 10
	- ``data[0:3, :]``: rows up to 3 (i.e. 0-2) of all columns
- Arrays have attributes:
	- ``data.shape``: the dimensions of the array ``data`` (rows, cols)
	- ``data.dtype``: the data type of elements in ``data``

### Working with lists

- 

---

## Doing Things basics

### Functions

- Not all functions take input (arguments).
- ``%``: denotes a IPython magic function, which is only valid within the notebook
   environment

### Libraries

- ``import numpy``: accesses the library ``numpy`` (NumPy) and loads it up for use. 
   "Importing a library is like getting a piece of lab equipment out of a storage locker 
   and setting it up on the bench." (Software Carpentry)
	- ``import matplotlib.pyplot``: imports the ``pyplot`` module from the ``matplotlib``
	   library
- ``numpy.mean()``: the function ``mean()`` drawn from library ``numpy``.
- ``numpy. \t``: In IPython and Jupyter Notebook, you can use tab completion to get a
   list of all functions in a library or attributes in an object.
- 


----

## Visualization

### matplotlib.pyplot


----

## 

----

## Functions by library

- `copy`
	- `copy.copy(x)`: Shallow copy operation.
	- `copy.deepcopy(x)`: Deep copy operation. 
- ``matplotlib``
	- 
- ``numpy``
	- ``numpy.max()``: 
		- ``numpy.max(data[2, :]))``
		- ``patient_0.max()``
- ``time``
	- ``time.ctime()``: current date & time
	
	
	