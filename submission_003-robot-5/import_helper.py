import sys
from importlib import import_module
  
# dynamic import  
def dynamic_import(name):
    if (name == "turtle" or name == "text"):
        name = "obstacles"

    if (name.startswith("test_") or name.startswith("tests/")):
        name = "obstacles"
    return import_module("maze." + name)
    
