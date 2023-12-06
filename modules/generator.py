# Imports
from typing import TextIO # type hinting for file object
from models.statements import *

# CodeGenerator class
class CodeGenerator:
    AST = [] # parsed AST
    filename = "" # output filename

    # constructor
    def __init__(self, AST: list, filename: str = "output/output.py") -> None:
        self.AST = AST # parsed AST
        self.filename = filename # output filename
    
    # generate python code from the parsed AST
    def generate(self) -> None:
        with open(self.filename, "w") as file:
            self.generate_recursively(file, self.AST)
    
    # recursive function to generate python code from the AST
    def generate_recursively(self, file: TextIO, AST: list, indent: int = 0) -> None: 
        for item in AST: # iterate through the parsed AST
            if isinstance(item, list): # if item is a list, then it is a block of code
                self.generate_recursively(file, item, indent + 1) # recursive call
            else:
                file.write("\t" * indent + str(item) + "\n") # write to file
