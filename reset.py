import os, stat, shutil
from subprocess import call
import venv
import pip

import platform
isWindows = platform.system() == "Windows"

def shell(command):
    return call(command.split(' '))

# helper function that allows deleting read only files when using rmtree
def remove_readonly(func, path, excinfo):
    os.chmod(path, stat.S_IWRITE)
    func(path)

if os.path.exists('env'):
    shutil.rmtree('env', onerror=remove_readonly)

if os.path.exists('newapp'):
    shutil.rmtree('newapp', onerror=remove_readonly)

os.chdir('myapp')
for filename in ['stackoverflow.py', 'requirements.txt', '.gitignore', 'survey2017.csv']:
    if os.path.exists(filename):
        os.remove(filename)

if os.path.exists('.git'):
    shutil.rmtree('.git', onerror=remove_readonly)

if isWindows:
    shell('env/scripts/python -m pip uninstall -y requests')
else:
    shell('env/bin/python -m pip uninstall -y requests')

# reset hello-stackoverflow
os.chdir('../hello-stackoverflow')      

files = os.listdir(".")
for filename in files:
    if filename.endswith(".csv") or filename == 'data.json':
        os.remove(filename)
    
if os.path.exists('.vscode/launch.json'):
    os.remove(".vscode/launch.json")

if os.path.exists('.vscode/settings.json'):
    os.remove(".vscode/settings.json")

if os.path.exists('analysis.py'):
    os.remove("analysis.py")

shell("git stash")
shell("rm -rf app")

# reset stackoverflow-flask
os.chdir('../stackoverflow-flask')      
shell("git stash")
shell("git checkout master")

if os.path.exists('.vscode/launch.json"'):
    os.remove(".vscode/launch.json")

shell("git stash")
shell("rm Dockerfile docker-compose.yml docker-compose.debug.yml .dockerignore")
