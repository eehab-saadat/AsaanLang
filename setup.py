import subprocess

subprocess.run(['npm', 'install','--save-dev'], shell=True)
subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
