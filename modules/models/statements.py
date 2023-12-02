class ASSIGNMENT_STATEMENT:
    variable_name = ""
    value = ""
    equiv_repr = ""

    def __init__(self, variable_name: str, value: str) -> None:
        self.variable_name = variable_name
        self.value = value
        self.equiv_repr = f"{variable_name} = {value}"

    def __str__(self) -> str:
        return f"{self.equiv_repr}"
    
    def __repr__(self) -> str:
        return f"ASSIGNMENT_STATEMENT({self.variable_name}, {self.value})"

class INPUT_STATEMENT:
    variable_name = ""
    equiv_repr = ""

    def __init__(self, variable_name: str) -> None:
        self.variable_name = variable_name
        self.equiv_repr = f"{variable_name} = input()"

    def __str__(self) -> str:
        return f"{self.equiv_repr}"
    
    def __repr__(self) -> str:
        return f"INPUT_STATEMENT({self.variable_name})"

class PRINT_STATEMENT:
    value = ""
    equiv_repr = ""

    def __init__(self, value: str) -> None:
        self.value = value
        self.equiv_repr = f"print({value})"

    def __str__(self) -> str:
        return f"{self.equiv_repr}"
    
    def __repr__(self) -> str:
        return f"PRINT_STATEMENT({self.value})"

class IF_STATEMENT:
    condition = ""
    equiv_repr = ""

    def __init__(self, condition: str) -> None:
        self.condition = condition
        self.equiv_repr = f"if {condition}:"

    def __str__(self) -> str:
        return f"{self.equiv_repr}"
    
    def __repr__(self) -> str:
        return f"IF_STATEMENT({self.condition})"

class ELIF_STATEMENT:
    condition = ""
    equiv_repr = ""

    def __init__(self, condition: str) -> None:
        self.condition = condition
        self.equiv_repr = f"elif {condition}:"

    def __str__(self) -> str:
        return f"{self.equiv_repr}"
    
    def __repr__(self) -> str:
        return f"ELIF_STATEMENT({self.condition})"
    
class ELSE_STATEMENT:
    equiv_repr = ""

    def __init__(self) -> None:
        self.equiv_repr = f"else:"

    def __str__(self) -> str:
        return f"{self.equiv_repr}"
    
    def __repr__(self) -> str:
        return f"ELSE_STATEMENT()"

class WHILE_STATEMENT:
    condition = ""
    equiv_repr = ""

    def __init__(self, condition: str) -> None:
        self.condition = condition
        self.equiv_repr = f"while {condition}:"

    def __str__(self) -> str:
        return f"{self.equiv_repr}"
    
    def __repr__(self) -> str:
        return f"WHILE_STATEMENT({self.condition})"