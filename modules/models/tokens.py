
class KEYWORD:
    name = ""
    equiv_repr = ""

    # lists of allowed keywords
    conditional_keyword = {"agar": "if", "jabtak": "while", "warnaagar": "elif"}
    other_keywords = {"likho": "print", "warna": "else", "btao?": "input"}
    var_types=["number", "lafz", "ishariya", "boolean"]

    def __init__(self, keyword: str, equiv_repr: str) -> None:
        self.name = keyword
        self.equiv_repr = equiv_repr

    def __repr__(self) -> str:
        return f"KEYWORD({self.name}, {self.equiv_repr})"

    def __str__(self) -> str:
        return f"{self.name}"

    def isConditional(self) -> bool:
        return self.name in self.conditional_keyword.keys()
    
    def isOther(self) -> bool:
        return self.name in self.other_keywords.keys()
    
    def isVarType(self) -> bool:
        return self.name in self.var_types
    
    def isJabTak(self):
        return self.name == "jabtak"
    
    def isAgar(self):
        return self.name == "agar"
    
    def isWarnaAgar(self):
        return self.name == "warnaagar"
    
    def isWarna(self):
        return self.name == "warna"
    
class OPERATOR:
    operator = ""
    equiv_repr = ""

    # lists of allowed operators
    assignment_op={"hai": "="}
    arithematic_op = ["+", "-", "*", "/", "%"]
    relational_op = {"keBrabar": "==", "keBrabarNahi": "!=", "seBara": "<", "seChota": ">", "jitnaYaChota": ">=", "jitnaYaBara":"<="}
    logical_op = {"aur": "and", "ya": "or", "nahi": "not"}

    def __init__(self, operator: str) -> None:
        self.operator = operator
        if operator in self.logical_op.keys():
            self.equiv_repr = self.logical_op[operator]
        elif operator in self.relational_op.keys():
            self.equiv_repr = self.relational_op[operator]
        elif operator in self.assignment_op.keys():
            self.equiv_repr = self.assignment_op[operator]
        else:
            self.equiv_repr = operator
    
    def __repr__(self) -> str:
        return f"OPERATOR({self.operator}, {self.equiv_repr})"
    
    def __str__(self) -> str:
        return f"{self.equiv_repr}"
    
    def isAssignment(self) -> bool:
        return self.operator == "hai"
    
    def isArithematic(self) -> bool:
        return self.operator in self.arithematic_op
    
    def isRelational(self) -> bool:
        return self.operator in self.relational_op
    
    def isLogical(self) -> bool:
        return self.operator in self.logical_op.keys()

class BOOL_KW:
    bool_val = {"sahi": "True", "galat": "False"}
    equiv_repr = ""

    def __init__(self, value: str) -> None:
        self.equiv_repr = self.bool_val[value]
    
    def __repr__(self) -> str:
        return f"BOOL_KW({self.equiv_repr})"
    
    def __str__(self) -> str:
        return f"{self.equiv_repr}"

class CONDITIONAL_EXP:
    condition = []
    equiv_repr = ""

    def __init__(self, condition: list) -> None:
        self.condition = condition
        self.equiv_repr = " ".join(str(condition))

    def __repr__(self) -> str:
        return f"CONDITIONAL_EXP({self.condition})"

    def __str__(self) -> str:
        return f"{self.equiv_repr}"
    
class COMMENT:
    equiv_repr = ""

    def __init__(self, comment: str) -> None:
        self.equiv_repr = comment

    def __repr__(self) -> str:
        return f"COMMENT({self.equiv_repr})"
    
    def __str__(self) -> str:
        return f"{self.equiv_repr}"
