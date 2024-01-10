# Imports
from subprocess import call

class Runner: # Runs the code
    input_file = "" # Path to the file to be run
    output_file = "" # Path to the file where the output will be written
    isCLI = False # if true, the output will be written to the console instead of a file

    # Constructor
    def __init__(self, isCLI: bool = False ,input_file: str = "transpiler/output/output.py", output_file: str= "backend/output/output.txt") -> None:
        self.input_file = input_file # path to the file to be run
        self.output_file = output_file # path to the file where the output will be written
        self.isCLI = isCLI # if true, the output will be written to the console instead of a file

    # Runs the code
    def run(self): 
        if not self.isCLI: # if output is to be written to a file
            with open(self.output_file, "w+") as output: # open the output file
                call(["python",f"./{self.input_file}"], stdout=output) # run the code and write the output to the file
        else: # if output is to be written to the console
            call(["python", f"./{self.input_file}"]) # run the code and write the output to the console
