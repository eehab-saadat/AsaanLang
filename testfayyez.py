from modules.models.statements import ASSIGNMENT_STATEMENT
from modules.generator import CodeGenerator

a = ASSIGNMENT_STATEMENT("a","10")
ast = [a]
CodeGenerator(ast).generate()