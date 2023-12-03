from modules.lexer import Lexer
from modules.tokenizer import Tokenizer

with open("samples/sample.alif", "r") as file:
    source_code = file.read()

expr_list = Lexer(source_code).lexicalize()
print(expr_list)
tokenized_list = Tokenizer(expr_list).tokenize()
print(tokenized_list)