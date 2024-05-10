import subprocess

commands = [('flask run','web-app'), ('npm run dev', 'web-app/frontend')]

for j in range(len(commands)):
    procs = [subprocess.Popen(command, shell = True, cwd = path) for command, path in commands]
    for p in procs:
        p.wait()