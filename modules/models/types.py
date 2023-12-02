class VARIABLE:
    name = ""
    type = ""
    allowed_operators = []

    def __init__(self, name, type, allowed_operators) -> None:
        self.name = name
        self.type = type
        self.allowed_operators = allowed_operators

    def __repr__(self) -> str:
        return f"VARIABLE({self.name}, {self.type}, {self.allowed_operators})"

    def __str__(self) -> str:
        return f"{self.name}"

class NUMBER(VARIABLE):
    def __init__(self, name) -> None:
        type = "NUMBER"
        allowed_operators = ["+", "-", "*", "/", "%"]
        super().__init__(name, type, allowed_operators)

class ISHARIYA(VARIABLE):
    def __init__(self, name) -> None:
        type = "ISHARIYA"
        allowed_operators = ["+", "-", "*", "/"]
        super().__init__(name, type, allowed_operators)

class LAFZ(VARIABLE):  
    def __init__(self, name) -> None:
        type = "LAFZ"
        allowed_operators = ["+"]
        super().__init__(name, type, allowed_operators)

class BOOLEAN(VARIABLE):
    def __init__(self, name) -> None:
        type = "BOOLEAN"
        allowed_operators = ["aur", "ya", "nahi"]
        super().__init__(name, type, allowed_operators)