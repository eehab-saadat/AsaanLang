class CodeGenerator:
    AST = []
    indent = 0

    def __init__(self, AST):
        self.AST = AST
    
    def generate(self, filename: str = "") -> None:
        pass