class Lexer:
    source_code = ""
    # index = 0
    # bracket stack

    def __init__(self, source_code: str):
        self.source_code = source_code
    
    def lexicalize(self) -> list:
        return self.source_code.split()
    
    # recusrively call lexcialize for code blocks and conditionals
    # recusrively call lexicalize if "{" is found for code block
    # recusrively call lexicalize if "(" is found for conditional
    
    # make a move function
    # def move(self) -> str:
    #     self.index += 1
    #     return self.source_code[self.index]

    # getWord function
    # getNumber function
