import subprocess

commands = ['flask run', 'npm start']

n=2

for j in range(max(int(len(commands)/n),1)):
    procs=[subprocess.Popen(i,shell=True) for i in commands[j*n:min((j+1)*n,len(commands))]]
    for p in procs:
        p.wait()