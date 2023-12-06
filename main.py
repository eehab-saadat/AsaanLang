from modules.lexer import Lexer
from modules.tokenizer import Tokenizer
from modules.parser import Parser
from modules.generator import CodeGenerator
from modules.models.statements import ASSIGNMENT_STATEMENT


import sys
sys.path.insert(0, "D:\AsaanLang\samples") #appropriate file path

with open("samples\sample.alif", "r") as file:
    source_code = file.read()

expr_list = Lexer(source_code).lexicalize()
print("Lexicalized AST:")
print(expr_list, end="\n\n")
tokenized_list, symbol_table = Tokenizer(expr_list).tokenize()
print("Tokenized AST:")
print(tokenized_list, end="\n\n")
print("Symbol Table:")
print(symbol_table)

AST = Parser(tokenized_list, symbol_table).parse() #implementation of Parser missing
code_generation = CodeGenerator(AST)
code_generation.generate('output.py')

#executes generated .py file // add relevant file path

# with open('D:\AsaanLang\output\output.py') as f: #import appropriate filepath or module
#     exec(f.read())