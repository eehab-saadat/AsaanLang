# CODE :
# number a hai 10
# number b hai btao?
# boolean c hai sahi
# jabtak (a seChota 0 aur b seBara 10) {
#     # Ek Tabsarah
#     likho "Salam Duniya!"
#     agar (a keBrabar 5) {
#         likho "a is 5"
#     } 
#     warnaagar (a keBrabar 6) {
#         likho "a is 6"
#     } 
#     warna {
#         likho "a is not 5 or 6"
#     }
#     a hai a - 1
# }

'''Tokenized_list :
[
    ["number", "a", OPERATOR, "10"], 
    ["number", "b", OPERATOR, KEYWORD], 
    ["boolean", "c", OPERATOR, BOOL_KW],
    [KEYWORD, CONDITIONAL_EXP], 
    [
        COMMENT,
        [KEYWORD, "Salam Duniya!"],
        [KEYWORD, CONDITIONAL_EXP], 
        [
            [KEYWORD, "a is 5"]
        ], 
        [KEYWORD, CONDITIONAL_EXP], 
        [
            [KEYWORD, "a is 6"]
        ], 
        [KEYWORD], 
        [
            [KEYWORD, "a is not 5 or 6"]
        ], 
        ["a", OPERATOR, "a", OPERATOR, "1"]
    ]
]
'''
'''PARSED AST: -> list to be returned by the parser
[
    ASSIGNMENT_STATEMENT, 
    INPUT_STATEMENT, 
    ASSIGNMENT_STATEMENT,
    WHILE_STATEMENT, 
    [
        COMMENT,
        PRINT_STATEMENT, 
        IF_STATEMENT, 
        [
            PRINT_STATEMENT
        ], 
        ELIF_STATEMENT, 
        [
            PRINT_STATEMENT
        ], 
        ELSE_STATEMENT, 
        [
            PRINT_STATEMENT
        ], 
        ASSIGNMENT_STATEMENT
    ]
]
'''

from models.tokens import *
from models.statements import *
from models.errors import *
from models.types import *

class Parser:
    tokenized_list = []
    symbol_table = []
    AST = [] # will contain the parsed AST
    current_line: int = 0 # to keep track of the current line number of source code

    def __init__(self, tokenized_list: list, symbol_table: list) -> None:
        self.tokenized_list = tokenized_list
        self.symbol_table = symbol_table
        self.AST = []
    
    def parse(self) -> list:
        self.parseRecursive(self.tokenized_list, self.AST)
        return self.AST
    
    def HasSameType(self, var1: str, var2:str) -> bool:
        return var1.type == var2.type
    
    def isFoundInSymbolTable(self, var_name:str) -> tuple:
        # if var_name matches variable.name in symbol table then return true,variable.type
        # else return false, None 
        for variable in self.symbol_table:
            if var_name == variable.name:
                return (True, variable.type)
            return (False,None)

    def isAllowedVariableName(self, var_name:str) -> bool:
        # variable name must start with a alphabet
        if not var_name[0].isalpha():
            return False
        # variable name must not contain any special character except underscore
        if not all(char.isalnum() or char == '_' for char in var_name):
            return False
        # variable name must not be a keyword
        if var_name in KEYWORD.other_keywords or var_name in KEYWORD.var_types or var_name in KEYWORD.conditional_keyword:
            return False
        return True

    def getVariable(self, var_name:str) -> VARIABLE:
        for variable in self.symbol_table:
            if var_name == variable.name:
                return variable
        return None
    
    def isAllowedOPerator(self, operator: str, allowed_operators:list) -> bool:
        if operator in allowed_operators:
            return True
        return False
    
    def isFloat(self, value:str):
        float_value = float(value)
        # Check if the string is numeric and contains a dot with no other characters
        return '.' in value and value.count('.') == 1 and value.replace('.', '').isdigit()
      
    # TO BE IMPLEMENTED
    def isAllowedAssignment(self, assignment_type: str, exp: list, allowed_operators: list) -> bool:
        # check if expression if valid
        if len(exp) == 0: # there is no expression to assign
            return False
        for i in range(len(exp)):
            if isinstance(exp[i], str):
                # either it is a variable in the symbol table
                variable = self.getVariable(exp[i])
                if variable is None: # variable not found
                    # string must adhere to the contranints of given type (string or int or float). return false if it doesnt
                    if assignment_type == "number" and not exp[i].isnumeric():
                        return False
                    elif assignment_type == "ishariya" and not self.isFloat(exp[i]):
                        return False
                    elif assignment_type == "lafz" and not exp[i].isalpha():
                        return False
                # is a variable
                elif variable.type.lower() != assignment_type:
                    return False
            
            elif isinstance(exp[i], OPERATOR):
                # operator must be between two operands
                if i-1 < 0 or i+1 >= len(exp) or not isinstance(exp[i-1], str) or not isinstance(exp[i+1], str) : 
                    return False
                # illegeal operator
                if not self.isAllowedOPerator(exp[i], allowed_operators):
                    return False
            
        return True     
                
    # TO BE IMPLEMENTED
    def isAllowedConditional() -> bool:
        return True

    def parseRecursive(self, tokens:list, AST:list) -> list:

        # Traverse till the end of tokenized list
        for i in range(len(tokens)):
            # if ith element of list is another list then recursive call
            if isinstance(tokens[i], list):
                self.current_line+=1
                self.parseRecursive(tokens[i])
            else:
                # handle all cases here

                # Note: multiple declarations and invalid variable names are already handled in the tokenizer
                # case 1: declaration statement
                # 1.1: type name
                # 1.2: type name hai value
                # 1.3: type name hai btao?

                # expect a declarative assignment statement
                if isinstance(tokens[i], str) and tokens[i] in KEYWORD.var_types: 
                    i+=1 # increment to variable name
                    if i >= len(tokens) or not isinstance(tokens[i], str):
                        pass # raise error expected a variable name
                    ##variable = (tokens[i], tokens[i-1]) # varaible(name, type)
                    variable = self.getVariable(tokens[i])
                    if variable is None: # (if error in tokenizer)
                        pass # raise error variable not found in symbol table
                    i+=1 # increment to assignment operator
                    if i>=len(tokens) or not isinstance(tokens[i], OPERATOR) or not tokens[i].isAssignment():
                        pass # raise assignment operator expected after declaration
                    # take all the tokens till end of line
                    # either it is a btao? keyword or a vlaue whose type should match the variable type
                    i+=1 # increment to btao? or expression
                    if i >= len(tokens):
                        pass # raise error expected an expression
                    if tokens[i] in KEYWORD.other_keywords and tokens[i].name == "btao?" :
                        # append and input statement to the AST
                        if i+1 >= len(tokens) : # to make sure nothing follows the btao? keyword
                            variable_type=""
                            if variable.type.lower() == "number":
                                variable_type.lower() == "int"
                            elif variable.type.lower() == "lafz":
                                variable_type.lower() == "str"
                            elif variable.type.lower() == "ishariya":
                                variable_type.lower() == "float"
                            else:
                                variable_type = "bool"
                            AST.append(INPUT_STATEMENT(variable.name, variable_type))
                        else :
                            pass # raise error: invalid input syntax (smth folloes the input statement in source code)
                    # is an expression
                    # for int | float | string
                    elif variable.type.lower() != "boolean" and self.isAllowedAssignment(variable.type, tokens[i:], variable.allowed_operators):
                        # append the assignment statement to the AST
                        AST.append(ASSIGNMENT_STATEMENT(variable.name, tokens[i:]))
                    # for boolean
                    elif self.isAllowedConditional():
                        # append the assignment statement to the AST
                        AST.append(ASSIGNMENT_STATEMENT(variable.name, tokens[i:]))
                    else:
                        pass # raise error invalid declaration

                # case 3 :for expression -> check if expression if valid or not
                # 3.1 is str
                # 3.2 i an operator

                # case 2: keyword statement
                # 2.2: while statement:
                # must be followed by a conditional
                # must be followed by a block-statement
                # call recursion with and empty list passed, append that list to the self.AST
                # 2.3: conditional statement:
                # 2.3.1: if statement:
                # must be followed be a conditional 
                #




        return self.AST