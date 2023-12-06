from modules.models.tokens import OPERATOR, BOOL_KW, CONDITIONAL_EXP, COMMENT, KEYWORD
from modules.models.types import NUMBER, ISHARIYA, LAFZ, BOOLEAN
from modules.models.errors import ERROR

# For Code Tokenizaion
class Tokenizer:
    expr_list = ""
    symbol_table = {}
    vars = []
    conditional_keyword = {"agar": "if", "jabtak": "while", "warnaagar": "elif"}
    other_keywords = {"likho": "print", "warna": "else", "btao?": "input"}
    var_types = ["number", "lafz", "ishariya", "boolean"]
 
    def __init__(self, expr_list: str) -> None:
        self.expr_list = expr_list

    def tokenize(self) -> tuple:
        return self.tokenizeRecursively(self.expr_list)

    def tokenizeRecursively(self, expression_list: list) -> tuple:
        # iterate through list
        for i in range(len(expression_list)):
            # if nested list found iterate through hat list
            if type(expression_list[i])==list:
                self.tokenizeRecursively(expression_list[i])
            else:
                # check for arithmetic and assignment operator
                if expression_list[i] in OPERATOR.arithematic_op or expression_list[i] in OPERATOR.assignment_op:

                    expression_list[i] = OPERATOR(expression_list[i])
                # check for relational operators and logical
                elif expression_list[i] in OPERATOR.relational_op or expression_list[i] in OPERATOR.logical_op:

                    expression_list[i]=OPERATOR(expression_list[i])

                # check boolean keywords
                elif expression_list[i] in BOOL_KW.bool_val:

                    expression_list[i] = BOOL_KW(expression_list[i])
                # check for conditional keywords
                elif expression_list[i] in self.conditional_keyword:

                    expression_list[i] = KEYWORD(expression_list[i],self.conditional_keyword[expression_list[i]])
                    self.tokenizeRecursively(expression_list[i+1])
                    expression_list[i+1] = CONDITIONAL_EXP(expression_list[i+1])
                # check for other keywords
                elif expression_list[i] in self.other_keywords:

                    expression_list[i] = KEYWORD(expression_list[i], self.other_keywords[expression_list[i]])
                # check for comments
                elif type(expression_list[i])==str:
                    if("#" in expression_list[i]):
                        expression_list[i] = COMMENT(expression_list[i])
                    # symbol table checking
                    elif expression_list[i].lower() in self.var_types:
                        # in case of multiple declarations throw error
                        if expression_list[i+1] in self.vars:
                            raise ERROR("error", "eek hi naam ke variable ko do martaba nahi banaya ja sakta")
                         # keyword as variable names check
                        if expression_list[i+1] in self.conditional_keyword or expression_list[i+1] in self.other_keywords:
                            raise ERROR("error", "variable ka name keyword nahi ho sakta")
                        # maintaining list of declaared variables
                        self.vars += expression_list[i+1]
                        # checking variable type
                        if expression_list[i].lower() == "number":
                            self.symbol_table.__setitem__(expression_list[i+1],NUMBER(expression_list[i+1]))
                        elif expression_list[i].lower() == "ishariya":
                            self.symbol_table.__setitem__(expression_list[i+1],ISHARIYA(expression_list[i+1]))
                        elif expression_list[i].lower() == "lafz":
                            self.symbol_table.__setitem__(expression_list[i+1],LAFZ(expression_list[i+1]))
                        elif expression_list[i].lower() == "boolean":
                            self.symbol_table.__setitem__(expression_list[i+1],BOOLEAN(expression_list[i+1]))
        result = (self.expr_list, self.symbol_table)
        return result



