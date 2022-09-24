# How to zip folder contain sub folder 
from pathlib import Path
import zipfile

sourceDir = Path('sourceDir/root_dir')

with zipfile.ZipFile('./outputDir/rootDir.zip','w') as archive:
    # rglob() - recursively traverse through dir 
    for file in sourceDir.rglob('*'):
        # file.relative_to(sourceDir) - get all all related to that directory
        archive.write(file, arcname= file.relative_to(sourceDir))

with zipfile.ZipFile('./outputDir/rootDir.zip','r') as archive:
    archive.printdir()