import zipfile

# the file should be present at current folder
fileNames = ["hello.txt", "mydata", "zipFileManipulation.py"]

# create a zipFile 
with zipfile.ZipFile("multipleFile.zip",'w') as archive:
    for file in fileNames:
        archive.write(file)
    print('Zip File is created successfully.')
# add file to your ZipFile 
with zipfile.ZipFile('multipleFile.zip','a') as archive:
    archive.write('pathLib.py')
    print('File appended successfully.')

# access files in specific directory 
# from pathlib import Path 

sourceDirectory = '/home/ubuntu/workspace/myWork/python/directory'
with zipfile.ZipFile('directoryFile.zip','w') as archive:
    for file_path in sourceDirectory.iterdir():
        archive.write(file_path,arcname=file_path.name)

