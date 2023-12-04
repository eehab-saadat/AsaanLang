import subprocess


class Runner:
    input_file = ""
    output_file = ""
    isCLI = False

    def __init__(self, isCLI: bool = False ,input_file: str = "output/output.py", output_file: str= "output/output.txt") -> None:
        self.input_file = input_file
        self.output_file = output_file
        self.isCLI = isCLI

    def run(self):
        if not self.isCLI:
            with open(self.output_file, "w+") as output:
                subprocess.call(["python",f"./{self.input_file}"], stdout=output)
        else:
            subprocess.call(["python", f"./{self.input_file}"])
