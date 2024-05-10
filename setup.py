import subprocess

subprocess.run(['npm', 'install'], shell=True, cwd='./web-app/frontend')
subprocess.run(['pip', 'install', '-r', 'requirements.txt'], cwd='web-app')

print("Dependencies installed successfully!")