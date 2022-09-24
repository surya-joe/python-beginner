from pprint import pprint


import pprint

cat = {
    'name' : 'Bell',
    'color': 'orange',
    'legs' : 4
}

# pretty printing
pprint.pprint(cat)
# keys()-Method 
for key in cat.keys():
    print(f'key => {key}')
# values()-Method 
for value in cat.values():
    print(f'value => {value}')
# items()-Method 
for item in cat.items():
    print(f'item => {item}')
# iterate over key:values pair 
for key,value in cat.items():
    print(f'key : {key} & value : {value}')
# get('key')-Method 
print(f"Name : {cat.get('name')}")
# none-key value 
print(f"None Key-value : {cat.get('tail','long')}")

# setDefault()- Method
# normal method 
if 'has_tail' not in cat:
    cat['has_tail'] = 'long'
print(cat)
# using setdefault()
cat.setdefault('eyes' , 2)
print(cat)

# pop()
cat.pop('name')
print(cat)

#  popItem()
cat.popitem()
print(cat)

# del()
del cat['color']
print(cat)

wife = {'name': 'Rose', 'age': 33, 'has_hair': True, 'hair_color': 'brown', 'height': 1.6, 'eye_color': 'brown'}
pprint.pprint(wife)

# merge dictionary 
dict1 = { 'name':'steve', 'age':25 }
dict2 = { 'height':170, 'color':'tan' }
dictMerge ={**dict1,**dict2}
print(dictMerge)

