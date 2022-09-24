import zipfile

sourceFile = './sourceDir/sampleZipFile.zip'

with zipfile.ZipFile(sourceFile,'r') as archive:
    # Extract all file in the zipFile 
    archive.extractall('./outputDir/sampleZipFile')
    print('Zip file extracted successfully.')
    # To get specific file get extracted
    for file in archive.namelist():
        if file.endswith('.txt'):
            archive.extract(file,'./outputDir/specZipFile')
    print('Specific Zip File extracted success.')
