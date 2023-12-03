from modules.models.tokens import OPERATOR, BOOL_KW, CONDITIONAL_EXP, COMMENT, KEYWORD
from modules.models.types import NUMBER, ISHARIYA, LAFZ, BOOLEAN

# For Code Tokenizaion
class Tokenizer:
    expr_list = ""
    symbol_table = []
    vars = []
    conditional_keyword = {"agar": "if", "jabtak": "while", "warnaagar": "elif"}
    other_keywords = {"likho": "print", "warna": "else", "btao?": "input"}
    var_types = ["number", "lafz", "ishariya", "boolean"]

    def __init__(self, expr_list: str) -> None:
        self.expr_list = expr_list

    def tokenize(self) -> tuple:
        return self.tokenizeRecursively(self.expr_list)

    def tokenizeRecursively(self, expressions: list) -> tuple:
        # iterate through list
        for i in range(len(expressions)):
            # if nested list found iterate through hat list
            if type(expressions[i])==list:
                self.tokenizeRecursively(expressions[i])
            else:
                # check for arithmetic and assignment operator
                if expressions[i] in OPERATOR.arithematic_op or expressions[i] in OPERATOR.assignment_op:

                    expressions[i] = OPERATOR(expressions[i])
                # check for relational operators
                elif expressions[i] in OPERATOR.relational_op:

                    expressions[i]=OPERATOR(expressions[i])

                # check boolean keywords
                elif expressions[i] in BOOL_KW.bool_val:

                    expressions[i] = BOOL_KW(expressions[i])
                # check for conditional keywords
                elif expressions[i] in self.conditional_keyword:

                    expressions[i] = KEYWORD(expressions[i],self.conditional_keyword[expressions[i]])
                    self.tokenizeRecursively(expressions[i+1])
                    expressions[i+1] = CONDITIONAL_EXP(expressions[i+1])
                # check for other keywords
                elif expressions[i] in self.other_keywords:

                    expressions[i] = KEYWORD(expressions[i], self.other_keywords[expressions[i]])
                # check for comments
                elif type(expressions[i])==str:
                    if("#" in expressions[i]):
                        expressions[i] = COMMENT(expressions[i])
                    # symbol table checking
                    elif expressions[i].lower() in self.var_types:
                        # in case of multiple declarations throw error
                        if expressions[i+1] in self.vars:
                            raise Exception("Multiple declaration not allowed")
                        # maintaining list of declaared variables
                        self.vars += expressions[i+1]
                        # checking variable type
                        if expressions[i].lower() == "number":
                            self.symbol_table.append(NUMBER(expressions[i+1]))
                        elif expressions[i].lower() == "ishariya":
                            self.symbol_table.append(ISHARIYA(expressions[i+1]))
                        elif expressions[i].lower() == "lafz":
                            self.symbol_table.append(LAFZ(expressions[i+1]))
                        elif expressions[i].lower() == "boolean":
                            self.symbol_table.append(BOOLEAN(expressions[i+1]))
        result = (self.expr_list, self.symbol_table)
        return result




