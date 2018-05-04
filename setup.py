import os, stat, shutil
from subprocess import call
import venv
import pip

def shell(command):
    return call(command.split(' '))

# helper function that allows deleting read only files when using rmtree
def remove_readonly(func, path, excinfo):
    os.chmod(path, stat.S_IWRITE)
    func(path)

# cleanup any previous demo files
for folder in ['hello-stackoverflow', 'myapp', 'newapp', 'env']:
    if os.path.exists(folder):
        shutil.rmtree('hello-stackoverflow', onerror=remove_readonly)

shell("git clone https://github.com/qubitron/hello-stackoverflow")
os.chdir("hello-stackoverflow")
venv.create("env", with_pip=True)
shell('env/scripts/python -m pip install -r requirements.txt')
os.chdir('..')

shell("git clone https://github.com/qubitron/stackoverflow-flask")
os.chdir("hello-stackoverflow")
venv.create("env", with_pip=True)
shell('env/scripts/python -m pip install -r requirements.txt')
os.chdir('..')

os.mkdir('myapp')
os.chdir('myapp')
venv.create("env", with_pip=True)
shell('env/scripts/python -m pip install pylint')
os.chdir('..')

snippetsPath = os.getenv('APPDATA') + '/code/user/snippets'
snippetsFile = snippetsPath + '/python.json'
if not os.path.exists(snippetsPath):
    os.mkdir(snippetsPath)

if os.path.exists(snippetsFile):
    # Merge the snippets in, blow away comments
    print("Merging snippets into existing code")
    venv.create("env", with_pip=True)
    shell('env/scripts/python -m pip install jstyleson')
    if shell('env/scripts/python mergesnippets.py') != 0:
        # something failed, blow away the snippets file
        shutil.copy('python.json', snippetsPath)
    shutil.rmtree('env', onerror=remove_readonly)
else:
    shutil.copy('python.json', snippetsPath)

