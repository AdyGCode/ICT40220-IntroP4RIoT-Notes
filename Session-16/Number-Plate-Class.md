# Number Plate

A class to generate random number plates for use in assessments, examples and more.

By: Adrian Gould >adrian.gould@nmtafe.wa.edu.au>
License: Creative Commons Share alike, No-Profit

## How to use

Import the class

```python
from number_plates import number_plates as NumberPlates
```

Instantiate class with default structure

> Default number plates of form LLL-NNN (3 letters, '-' and 3 numbers)

```python
number_plate = NumberPlates()
```

Instantiate class with 5 letters, 4 numbers and ':'

```python
big_plate = NumberPlates(letter_count=5, number_count=4, separator=":")
```

Named parameters allow you to reorder:

```python
different_plate = NumberPlates(letter_count=4, separator=":", number_count=4)
```


Create a new plate:

```python
car_plate = number_plate.create()
```

