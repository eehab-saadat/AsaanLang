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

# [ STatement ]
# AST = [ [statement] ]

'''Tokenized_list :
[
    ["number", "a", OPERATOR, "10"], 
    ["number", "b", OPERATOR, KEYWORD], 
    ["boolean", "c", OPERATOR, BOOL_KW],
    [KEYWORD, CONDITIONAL_EXP,  [
        [KEYWORD, "Salam Duniya!"],
    ]],
   
        
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
    symbol_table = {}
    AST = [] # will contain the parsed AST
    current_line: int = 0 # to keep track of the current line number of source code

    def __init__(self, tokenized_list: list, symbol_table: dict) -> None:
        self.tokenized_list = tokenized_list
        self.symbol_table = symbol_table
        self.AST = []
    
    def parse(self) -> list:
        self.parseRecursive(self.tokenized_list, self.AST)
        return self.AST
    
    # def HasSameType(self, var1: str, var2:str) -> bool:
    #     return var1.type == var2.type
    
    def isVariable(self, var_name:str) -> bool:
        if var_name in self.symbol_table:
            return True
        return False

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
        if var_name in self.symbol_table:
            return self.symbol_table[var_name]
        else:
            return None
        
    def isAllowedOPerator(self, operator: str, allowed_operators:list) -> bool:
        if operator in allowed_operators:
            return True
        return False
    
    def isFloat(self, value:str):
        float_value = float(value)
        # Check if the string is numeric and contains a dot with no other characters
        return '.' in value and value.count('.') == 1 and value.replace('.', '').isdigit()
      
    def isAllowedAssignment(self, assignment_type: str, exp: list, allowed_operators: list) -> bool:
        # check if expression if valid
        if len(exp) == 0: # there is no expression to assign
            return False
        for i in range(len(exp)):
            # if it is str 
            if isinstance(exp[i], str) :
                # either it is a variable in the symbol table:
                # then must not be followed by another string, only operators are allowed
                if i+1 < len(exp) and isinstance(exp[i+1], str):
                    return False
                variable = self.getVariable(exp[i])
                if variable is None: # variable not found
                    # string must adhere to the contranints of given type (string or int or float). return false if it doesnt
                    if assignment_type == "number" and not exp[i].isnumeric():
                        return False
                    elif assignment_type == "ishariya" and not self.isFloat(exp[i]):
                        return False
                # is a variable of wrong type
                elif variable.type.lower() != assignment_type:
                    return False
            
            elif isinstance(exp[i], OPERATOR):
                # illegeal operator
                if not self.isAllowedOPerator(exp[i].operator, allowed_operators):
                    return False
                # operator must be between two operands
                if i-1 < 0 or i+1 >= len(exp): 
                    return False
                if not isinstance(exp[i-1], str) or not isinstance(exp[i+1], str) : 
                    return False
            else:
                return False
            
        return True     

    def convertTOExpression(self, exp: list, var_type: str) -> str:
        resultant = ""
        var_type = var_type.lower()
        for i in range(len(exp)):
            if self.isVariable(exp[i]) :
                resultant += exp[i] + " "
            elif isinstance(exp[i], OPERATOR):
                resultant += exp[i].equiv_repr + " "
            # for boolean
            elif var_type == "boolean" and isinstance(exp[i], BOOL_KW):
                resultant += exp[i].equiv_repr + " "
            else : # is a constant term
                if var_type == "lafz": # for str type
                    resultant += f"\"{exp[i]}\" "
                else: # for int or float tye
                    resultant += exp[i] + " "

        return resultant
    
    def convertTOCondition(self, condition: list) -> str :
        resultant = ""
        for i in range(len(condition)):
            if self.isVariable(condition[i]) :
                resultant += condition[i] + " "
            elif isinstance(condition[i], OPERATOR) or isinstance(condition[i], BOOL_KW):
                resultant += condition[i].equiv_repr + " "
            # for boolean
            elif isinstance(condition[i], BOOL_KW):
                resultant += condition[i].equiv_repr + " "
            elif isinstance(condition[i], str) and condition[i].isnumeric() or self.isFloat(condition[i]):
                resultant += condition[i] + " "
            else : # is assume is a string
                resultant += f"\"{condition[i]}\" "

        return resultant
    
    # TO BE IMPLEMENTED
    def isAllowedConditional(self, condition: list) -> bool:
        # there is no condition
        if len(condition) == 0:
            return False
        # check if condition is valid
        for i in range(len(condition)):
            if isinstance(condition[i], BOOL_KW):
                if i+1 >= len(condition) -1 :
                # must not be succeeded by a str or another bool
                    return False
                if isinstance(condition[i+1], str) or isinstance(condition[i+1], BOOL_KW):
                    return False
            if isinstance(condition[i], str) and i+1 >= len(condition) or isinstance(condition[i+1], str) or isinstance(condition[i+1], BOOL_KW):
               return False
            if isinstance(condition[i], OPERATOR):

                if condition[i].isAssignment(): # assignment mid condition is not allowed in conditional
                    return False

                if condition[i].islogical() and condition[i].operator == "nahi" :
                    # must be followed by a string or bool_kw
                    if i+1 >= len(condition) or isinstance(condition[i+1], OPERATOR):
                        return False

                if condition[i].isArithematic() or condition[i].isRelational() or condition[i].isLogical() and condition[i].operator != "nahi" :
                    # must be preceeded and succeeded by a str
                    if i+1 >= len(condition) or i-1 < 0 or not isinstance(condition[i-1], str) or not isinstance(condition[i+1], str):
                        return False

        return True

    def parseRecursive(self, tokens:list, AST: list) -> list:

        # Traverse till the end of tokenized list
        for i in range(len(tokens)):
            # if ith element of list is another list then recursive call
            # if AST[-1] == while | if | elif :
            #   AST.append(tempAST)
            if isinstance(tokens[i], list):
                self.current_line += 1
                tempAST:list = []
                tempAST = self.parseRecursive(tokens[i], tempAST)
                if len(tempAST) == 1:
                    AST += tempAST
                else :
                    AST.append(tempAST)

            else:

                # for assignment or input statement statements
                if isinstance(tokens[i], str): # could be a variable name or type declaration
                    #if is a type declaration
                    if tokens[i] in KEYWORD.var_types: 
                        i+=1 # increment to variable name
                        # must be followed by a variable name
                        if i >= len(tokens) or not isinstance(tokens[i], str) or self.getVariable(tokens[i]) == None:
                            pass # raise error expected a variable name
                    ##variable = (tokens[i], tokens[i-1]) # varaible(name, type)
                    variable = self.getVariable(tokens[i])
                    if variable is None:
                        pass # raise error variable not found in symbol table (error in tokenizer)
                    i+=1 # increment to assignment operator
                    if i >= len(tokens) or not isinstance(tokens[i], OPERATOR) or not tokens[i].isAssignment():
                        pass # raise assignment operator expected after declaration
                    i+=1 # increment to btao? or expression
                    if i >= len(tokens):
                        pass # raise error expected a value
                    if isinstance(tokens[i], KEYWORD) and tokens[i].name == "btao?" :
                        # append an input statement to the AST
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
                            break
                        else :
                            pass # raise error: invalid input syntax (smth folloes the input statement in source code)
                    # is an expression
                    # evaluate expression for int | float | string
                    elif variable.type.lower() != "boolean" and self.isAllowedAssignment(variable.type, tokens[i:], variable.allowed_operators):
                        # append the assignment statement to the AST
                        exp = self.convertTOExpression(tokens[i:], variable.type)
                        AST.append(ASSIGNMENT_STATEMENT(variable.name, exp))
                        break
                    # for boolean
                    elif variable.type.lower() == "boolean" and self.isAllowedConditional():
                        # append the assignment statement to the AST
                        exp = self.convertTOExpression(tokens[i:], variable.type)
                        AST.append(ASSIGNMENT_STATEMENT(variable.name, exp))
                        break
                    else:
                        pass # raise error invalid assignment
  
                # 1--- code for conditional
                # 2 --- errors
                
                # for comments
                elif isinstance(tokens[i], COMMENT):
                   AST.append(tokens[i]) # append as it is

                # could be conditonal(if,elif,else), print or while loop
                elif isinstance(tokens[i], KEYWORD):

                    # for print statement
                    if tokens[i].name == "likho":
                        i+=1
                        #must be followed by a string or a single variable
                        if i == len(tokens) - 1:
                            statement_to_print = ""
                            # if variable
                            if self.isVariable(tokens[i]) :
                                statement_to_print = tokens[i]
                            # if string then wrap in quotation
                            elif isinstance(tokens[i], str):
                                statement_to_print = f"\"{tokens[i]}\""
                            else:
                                pass # raise error: token cannot be printed
                            AST.append(PRINT_STATEMENT(statement_to_print))
                            break
                        else :
                            pass # raise error: invalif print statement

                    # for while / if / elif statement or else -> check is followed by conditional
                    elif tokens[i].isConditional() or tokens[i].isWarna() :
                        # if is an elif | else statement (warnaagar) then -> must be preceeded by an if or elif statement
                        
                        keyword : KEYWORD = tokens[i]
                        condition : str = ""
                        # taking into account the condition for while | if | elif :
                        if keyword.isConditional():
                            i+=1
                            # if is a valid condition
                            if i != len(tokens) - 1 or not isinstance(tokens[i], CONDITIONAL_EXP) or not self.isAllowedConditional(tokens[i].condition):
                                pass # raise error: invalid conditional expression
                            condition : str = self.convertTOCondition(tokens[i].condition) # get the condition
                       
                        #append the statement to AST
                        if keyword.isJabTak():
                            AST.append(WHILE_STATEMENT(condition))
                        elif keyword.isAgar():
                            AST.append(IF_STATEMENT(condition))
                        elif keyword.isWarnaAgar():
                            AST.append(ELIF_STATEMENT(condition))
                        else:
                            AST.append(ELSE_STATEMENT())
                        break 

                    else :
                        pass # raise error: invalid keyword usage

                else:
                    pass # raise error: unidentified or invalid token
        
            
        # check that all while, if, elif , else statements are followed by a code block (list) in the ast
        for i in range(len(AST)):
            
            if isinstance(AST[i], list) :
                # must be preceeded by a while or if or elif statement
                if i-1 < 0 or not isinstance(AST[i-1], WHILE_STATEMENT) or not isinstance(AST[i-1], IF_STATEMENT) or not isinstance(AST[i-1], ELIF_STATEMENT):
                    pass # raise error: code block expected at 


        return AST
    
'''

'''
tempTable = {"a": NUMBER("a"), "b": NUMBER("b"), "c": LAFZ("c"),}

temptokens = [
        [KEYWORD("jabtak", "while"), CONDITIONAL_EXP(['a', OPERATOR('seChota'), '0', OPERATOR('aur'), 'b', OPERATOR('seBara'), '10'])], 
        [
            COMMENT("# Ek Tabsarah"),
            [KEYWORD("likho", 'print'), "Salam Duniya!"],
            [KEYWORD('agar', 'if'), CONDITIONAL_EXP(['a', OPERATOR('keBrabar'), '5'])], 
            [
                [KEYWORD('likho', 'print'), "a is 5"]
            ], 
            [KEYWORD('warnaagar', 'elif'), CONDITIONAL_EXP(['sahi'])], 
            [
                [KEYWORD('likho', 'print'), "a is 6"]
            ], 
            [KEYWORD('warna', 'else')], 
            [
                [KEYWORD('likho', 'print'), "a is not 5 or 6"]
            ], 
            ["a", OPERATOR('hai'), "a", OPERATOR('-'), "1"]

        ]
]

par = Parser(temptokens, tempTable).parse()
print(par[0:])