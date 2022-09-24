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
# iterdir() function 
from pathlib import Path 

sourceDirectory = Path('./sourceDir/multipleFile/')
with zipfile.ZipFile('./outputDir/directoryFile.zip','w') as archive:
    for file in sourceDirectory.iterdir():
        # arcname=file_path.name 
        archive.write(file,arcname=file.name)
    print('Directory zip file created successfully.')

with zipfile.ZipFile('./outputDir/directoryFile.zip') as archive:
    print(archive.printdir())
