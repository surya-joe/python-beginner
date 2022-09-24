import shelve

filePath = '/home/ubuntu/workspace/myWork/python/shelveFile.txt'
cats = ['Tom','Bonny','Rose']
with shelve.open('mydata') as file:
    file['cats'] = cats
    print(type(file))
    print(file['cats'])
    print('key:',list(file.keys()))
    print('value:',list(file.values()))