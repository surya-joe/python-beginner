from pathlib import Path
# Global fielPath
filePath = '/home/ubuntu/workspace/myWork/python/file.txt'
# create a new file using python 
if Path(filePath).exists():
    print('File already exist')
else:
    open('file.txt','a')
    print('File created successfully')
    
# ******************File Access Modes*****************
# 'r'-read only 
# 'r+'-read & write
# 'w'- write only (over-written the existing data)
# 'w+'- write & read (over-written the existing data)
# 'a'-append a new line at end on existing data 
# 'a+'-read & write mode.

# open file to read()
with open(filePath) as file:
    readFile = file.read()
    print('1:read\n',readFile)
# open file to append data 
with open(filePath,'a+') as file:
    writeFile = file.write('Writting a New line1\n') 
# open file to read everylines in a file 
with open(filePath,'r') as file:
    readFile = file.readlines()
    print('3:read-specific-Line\n',readFile[1])
    # iterate over each line in a file 
    print('++++++++++++++++iteration of lines++++++++++++++++')
    for index,item in enumerate(readFile):
        print(f'line:{index}',item)