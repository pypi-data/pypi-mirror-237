# pycutroh

_The pycutroh module is a simple string cutting module._

## Table of contents

1. [Introduction](#introduction)
2. [Getting started](#getting-started)
    1. [Prerequisites](#prerequisites)
    2. [Installation](#installation)
3. [How to use](#how-to-use)
    1. [How to import](#how-to-import)
    2. [Using the module](#using-the-module)
4. [License](/LICENSE)

## Introduction

I've written this module to learn python and some python basics like using unittests, imports and how python modules/packets work. 

This module is inspired by the linux bash command.

At the moment this module provides four functions, which can be used to manipulate strings. For further information see here: [How to use](#how-to-use)

The cli interface for this module only shows help at the moment and will be further expanded, as well as the package functionality itself.

## Getting started

### Prerequisites

- Python installed
- Operatingsystem: Linux or Windows, not tested on mac
- IDE like VS Code, if you want to contribute or change the code

### Installation

There are two ways to install this module depending on the way you work and the preinstalled modules:

1. ```pip install pycutroh```
2. ```python -m pip install pycutroh```

## How to use

### How to Import

You can import the module in two ways:

```python
import pycutroh
```

- This will import all functions. Even the ones that are not supposed to be used (helper functions).

```python
from pycutroh import *
```

- This will import only the significant functions, meant for using. 

### Using the module

Depending on the way you imported the module, the following examples look a bit different.

Example 1:

```python
from pycutroh import *

print(get_letter_on_pos("This is a demonstration string.",0))
```
Result:
```
T
```

Example 2:

```python
from pycutroh import *

print(get_letters_from_pos_to_pos("This is a demonstration string.",(0,4)))

```
Result:
```
This
```

Example 3:

```python
from pycutroh import *

print(get_fields("This is a demonstration string.",(0,3)," "))

```
Result:
```
This demonstration
```

Example 4:

```python
import pycutroh

print(pycutroh.get_fields_new_separator("This is a demonstration string.",(0,3)," ","|"))
```
Result:
```
This|demonstration
```
## License

[MIT](/LICENSE)