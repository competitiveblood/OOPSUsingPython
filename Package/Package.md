**BASIC DEFINITION**

Package in Python is a folder that contains various modules as files

**CREATING PACKAGE IN PYTHON**

Python package named mypckg containing modules mod1 and mod2

1) creating folder named mypckg
2) inside the folder,empty py file named __init__.py
3) create 2 modules mod1 and mod2 in the __init__.py folder 
4) Mod1.py

def gfg():
print("Welcome to GFG")

5) Mod2.py

def sum(a,b):
return a+b

6) from .mod1 import gfg
 from .mod2 import sum

This __init__.py will only allow the gfg and sum functions from the mod1 and mod2 modules to be imported.


Example=>
We will import the modules from the above-created package and will use the functions inside those modules 

## Example1
from mypckg import mod1
from mypckg import mod2
mod1.gfg()
res= mod2.sum(1,2)
print(res)

## Example 2
from mypckg.mod1 import gfg
from mypckg.mod2 import sum
gfg()
res = sum(1, 2)
print(res)
