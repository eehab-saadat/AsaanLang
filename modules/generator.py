import sys
sys.path.insert(0, "D:\AsaanLang\modules") #replace with appropriate module filepath
from modules.models.statements import ASSIGNMENT_STATEMENT
from models.statements import ASSIGNMENT_STATEMENT

# from models.statements import __str__
   

class CodeGenerator:
    AST = []
    indent = 0
    
    def __init__(self, AST):
        self.AST = AST

    def indent_level(self) -> int:      #returns current indent level
        return self.indent
    
    def indent_change(self) ->int:      #increments indent level
        self.indent = self.indent + 1
    
    def generate(self, filename: str = "") -> None:
        indent_num = self.indent_level()                #stores indent level in the beginning of the code generation #at which indent is 0
        print_list(self.AST, indent_num=indent_num)     #sends the list to function to be indented and replaced


def print_list(the_list, indent_num):

    secondfile = open(f'D:\AsaanLang\output\output.py', 'a')
    for each_item in the_list:
        if isinstance(each_item, list):
            secondfile.seek(0,0) 
            secondfile.write('\n')
            print_list(each_item, indent_num = indent_num + 1)
        else:
            secondfile.write(('\t' * indent_num) + each_item.__str__() + '\n') 
    secondfile.close()

        
a = ASSIGNMENT_STATEMENT("a", "2")
print(a)


'''
from output.py cache lines
'''
#import sys, ast, re
# sys.path.insert(0, "D:\AsaanLang\modules")

# from lexer import Lexer 
# from parser import Parser
# from tokenizer import Tokenizer

# import models 
# from models import __str__


    