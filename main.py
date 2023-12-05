from modules.lexer import Lexer
from modules.tokenizer import Tokenizer

with open("samples/sample.alif", "r") as file:
    source_code = file.read()

expr_list = Lexer(source_code).lexicalize()
print("Lexicalized AST:")
print(expr_list, end="\n\n")
tokenized_list, symbol_table = Tokenizer(expr_list).tokenize()
print("Tokenized AST:")
print(tokenized_list, end="\n\n")
print("Symbol Table:")
print(symbol_table)