from modules.lexer import Lexer
from modules.tokenizer import Tokenizer

with open("samples/sample.alif", "r") as file:
    source_code = file.read()

expr_list = Lexer(source_code).lexicalize()
tokenized_list = Tokenizer(expr_list).tokenize()

print(expr_list)
print(tokenized_list)