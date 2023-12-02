class Lexer:
    source_code = ""

    def __init__(self, source_code: str):
        self.source_code = source_code
    
    def lexicalize(self) -> list:
        return self.source_code.split()