class Parser:
    tokenized_list = []
    symbol_table = []

    def __init__(self, tokenized_list: list, symbol_table: list) -> None:
        self.tokenized_list = tokenized_list
        self.symbol_table = symbol_table
    
    def parse(self) -> list:
        pass