import os, jstyleson, platform

snippetsPath = ''
if platform.system() == 'Windows':
    snippetsPath = os.getenv('APPDATA') + '\\Code\\User\\snippets'
else:
    snippetsPath = os.path.expanduser("~/Library/Application Support/Code/User/snippets")
snippetsFile = snippetsPath + '/python.json'

result = {}
with open(snippetsFile) as targetFile:
    with open('python.json') as sourceFile:
        result = jstyleson.load(targetFile)
        source = jstyleson.load(sourceFile)

        for key in source:
            result[key] = source[key]

with open(snippetsFile, 'w') as targetFile:
    jstyleson.dump(result, targetFile, indent=4)
