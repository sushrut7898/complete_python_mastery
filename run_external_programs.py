import subprocess

completed = subprocess.run(["python","first.py"], capture_output=True,text=True,check=True)
print("args",completed.args)
print("returncode",completed.returncode)
print("stderr",completed.stderr)
print("stdout", completed.stdout)
#if Return code != 0 the theirs some error