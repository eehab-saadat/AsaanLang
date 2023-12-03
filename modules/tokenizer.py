from models import tokens
from models import types

class Tokenizer:
    expr_list = ""
    symbol_table = []
    vars = []
    conditional_keyword = {"agar": "if", "jabtak": "while", "warnaagar": "elif"}
    other_keywords = {"likho": "print", "warna": "else", "btao?": "input"}
    var_types=["number", "lafz", "ishariya", "boolean"]

    def __init__(self, expr_list: str) -> None:
        self.expr_list = expr_list

    def tokenize(self) -> tuple:
        return self.tokenizer(self.expr_list)

    def tokenizer(self, exprs):
        # iterate through list
        for i in range(len(exprs)):
            # if nested list found iterate through hat list
            if type(exprs[i])==list:
                self.tokenizer(exprs[i])
            else:
                # check for arithmetic and assignment operator
                if exprs[i] in tokens.OPERATOR.arithematic_op or exprs[i] in tokens.OPERATOR.assignment_op:

                    exprs[i] = tokens.OPERATOR(exprs[i])
                # check for relational operators
                elif exprs[i] in tokens.OPERATOR.relational_op:

                    exprs[i]=tokens.OPERATOR(exprs[i])

                # check boolean keywords
                elif exprs[i] in tokens.BOOL_KW.bool_val:

                    exprs[i] = tokens.BOOL_KW(exprs[i])
                # check for conditional keywords
                elif exprs[i] in self.conditional_keyword:

                    exprs[i] = tokens.KEYWORD(exprs[i],self.conditional_keyword[exprs[i]])
                    self.tokenizer(exprs[i+1])
                    exprs[i+1] = tokens.CONDITIONAL_EXP(exprs[i+1])
                # check for other keywords
                elif exprs[i] in self.other_keywords:

                    exprs[i] = tokens.KEYWORD(exprs[i], self.other_keywords[exprs[i]])
                # check for comments
                elif type(exprs[i])==str:
                    if("#" in exprs[i]):
                        exprs[i] = tokens.COMMENT(exprs[i])
                    # symbol table checking
                    elif exprs[i].lower() in self.var_types:
                        # in case of multiple declarations throw error
                        if exprs[i+1] in self.vars:
                            raise Exception("Multiple declaration not allowed")
                        # maintaining list of declaared variables
                        self.vars += exprs[i+1]
                        # checking variable type
                        if exprs[i].lower() == "number":
                            self.symbol_table.append(types.NUMBER(exprs[i+1]))
                        elif exprs[i].lower() == "ishariya":
                            self.symbol_table.append(types.ISHARIYA(exprs[i+1]))
                        elif exprs[i].lower() == "lafz":
                            self.symbol_table.append(types.LAFZ(exprs[i+1]))
                        elif exprs[i].lower() == "boolean":
                            self.symbol_table.append(types.BOOLEAN(exprs[i+1]))
        result = (self.expr_list, self.symbol_table)
        return result




