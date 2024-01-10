from subprocess import call
from argparse import ArgumentParser
from transpiler.transpiler import Transpiler

# create an argument parser
arg_parser = ArgumentParser(prog='python transpile.py', description='Asaanlang Transpiler [GitHub: https://github.com/eehab-saadat/AsaanLang]')
arg_parser.add_argument('-w', '--web', action='store_true', help='run asaanlang web app')
arg_parser.add_argument('-i', '--input', type=str, help="input file for running asaanlang code, accepts '.alif' files only")
arg_parser.add_argument('-o', '--output', type=str, help="output file for storing transpiled python code, accepts '.txt' files only")

input_file = "" # input file
output_file = "" # output file

args = arg_parser.parse_args() # parse the arguments
if args.web: # if the web app is to be run
    if args.input or args.output: # if i/o args are provided
        print("error: i/o args not required for running the web app")
    else: # else run the web app
        call(["python", f"./web-app.py"])
else: # else run the transpiler through the CLI
    if args.input: # if input arg is provided
        if args.input.endswith(".alif"): # if the input file has .alif extension
            input_file = args.input # set the input file
        else: # else throw an error
            print("error: input file must have .alif extension") # throw an error
    if args.output: # if output arg is provided
        if args.output.endswith(".txt") : # if the output file has .txt extension
            output_file = args.output # set the output file
        else: # else throw an error
            print("error: output file must have .txt extension")
    try:
        # transpiling through the CLI
        if input_file != "" and output_file != "": # if both input and output files are provided
            Transpiler(isClI=True, input_file=input_file, output_file=output_file).transpile()
        elif input_file != "": # if only input file is provided
            Transpiler(isCLI=True, input_file=input_file).transpile()
        elif output_file != "": # if only output file is provided
            Transpiler(isCLI=True, output_file=output_file).transpile()
        else: # if no i/o files are provided
            Transpiler(isCLI=True).transpile()
    except Exception as e:
        print(e)