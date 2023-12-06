from modules.lexer import Lexer
from modules.tokenizer import Tokenizer
from modules.parser import Parser
from modules.generator import CodeGenerator
from modules.runner import Runner
from modules.models.errors import ERROR

with open("samples/sample.alif", "r") as file:
    source_code = file.read()

# expr_list = Lexer(source_code).lexicalize()
# print("Lexicalized AST:")
# print(expr_list, end="\n\n")
# tokenized_list, symbol_table = Tokenizer(expr_list).tokenize()


expr_list = Lexer(source_code).lexicalize()
tokenized_list, symbol_table = Tokenizer(expr_list).tokenize()
print("Tokenized AST:")
print(tokenized_list, end="\n\n")
print("Symbol Table:")
print(symbol_table, end="\n\n")
try:
    parsered_AST = Parser(tokenized_list, symbol_table).parse()
    print("Parsed AST:")
    print(parsered_AST, end="\n\n")
    CodeGenerator(parsered_AST).generate()
    Runner(True).run()
except ERROR as error:
    print(error)