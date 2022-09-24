import zipfile

filePath = '/home/ubuntu/workspace/myWork/python/file.txt'
zipFilePath = '/home/ubuntu/workspace/myWork/python/sample.zip'

# # open zip-file and print_directory
# with zipfile.ZipFile(zipFilePath,'r') as archive:
#     print(archive.printdir())

# check file is a valid zip file or not usint try & except
try:
    with zipfile.ZipFile(filePath,'r')as archive:
        print('valid zip file\n',archive.printdir())
except zipfile.BadZipFile as error:
    print(error) 

# check file is a valid zip file or not usint if & else
# is_zipfile() function
if zipfile.is_zipfile(filePath):
    with zipfile.ZipFile(filePath,'r') as archive:
        print(archive.printdir())
else:
    print('Not a Valid zip-file')

# append a file into zipFile 
with zipfile.ZipFile(zipFilePath,'a') as archive:
    # the file which is to be appended must have in current directory 
    archive.write('pathLib.py')
    print('File appended successfully.')
    print(archive.printdir())

# print file names inside your zipfile 
with zipfile.ZipFile(zipFilePath,'r') as archive:
    # getinfo('fileName') function
    # for single file info use {file.getinfo('fileName')}
    info = archive.getinfo('hello.txt')
    print(f'File name : {info.filename}')
    print(f'File Size : {info.file_size}')
    print(f'Compress Size : {info.compress_size}')

#infolist() function
with zipfile.ZipFile(zipFilePath,'r') as archive:
    # for multiple file details use {file.infolist()}
    for info in archive.infolist():
        print(f'File name : {info.filename}')
        print(f'File Size : {info.file_size}')
        print(f'Compress Size : {info.compress_size}')