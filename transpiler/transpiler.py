from transpiler.modules.lexer import Lexer
from transpiler.modules.tokenizer import Tokenizer
from transpiler.modules.parser import Parser
from transpiler.modules.generator import CodeGenerator
from transpiler.modules.runner import Runner
from transpiler.modules.models.errors import ERROR

class Transpiler:
    isCLI = False
    input_file = ""
    output_file = ""
    source_code = ""

    def __init__(self, **kwargs) -> None:
        #  check if the transpiler is being run through the CLI or the web app
        if "isCLI" in kwargs:
            self.isCLI = kwargs["isCLI"]
        else:
            self.isCLI = False

        # set tjhe input file if the transpiler is being run through the CLI
        if "input_file" in kwargs and self.isCLI == True:
            self.input_file = kwargs["input_file"]
        else: # else set the default input file
            self.input_file = "transpiler/samples/calculator.alif"

        # set the output file if the transpiler is being run through the CLI
        if "output_file" in kwargs and self.isCLI == True:
            self.output_file = kwargs["output_file"]
        else:
            self.output_file = "transpiler/output/output.py"

        # set the source code if the transpiler is being run through the web app
        if "source_code" in kwargs and self.isCLI == False:
            self.source_code = kwargs["source_code"]
        else: # else set the default source code
            with open(f"{self.input_file}", "r") as file:
                self.source_code = file.read()

    # transpile the source code
    def transpile(self) -> None:
        try:
            lexicalized_ast = Lexer(self.source_code).lexicalize()
            tokenized_ast, symbol_table = Tokenizer(lexicalized_ast).tokenize()
            parsed_ast = Parser(tokenized_ast, symbol_table).parse()
            CodeGenerator(parsed_ast).generate()
            Runner(self.isCLI, self.output_file).run()
        except ERROR as error:
            print(error)