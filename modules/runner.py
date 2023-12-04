import subprocess


class Runner:
    input_file = ""
    output_file = ""

    def __init__(self, input_file: str, output_file: str) -> None:
        self.input_file = input_file
        self.output_file = output_file

    def run(self):
        with open(self.output_file, "w+") as output:
            subprocess.call(["python",f"./{self.input_file}"],stdout=output)
