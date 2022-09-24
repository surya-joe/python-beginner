import re
find_phone_num = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phone_num = find_phone_num.search('my 343-444 numer is 455-555-4241 , 211-244-111')
print(f'Phone numeber finded : {phone_num.group()}')

find_phone_num1 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
phone_num1 = find_phone_num1.search('my numer is 455-555-4241')
print(phone_num1.group(2))

# phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# mo = phone_num_regex.search('My number is 415-555-4242.')

# '|'symbol
bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = bat_regex.search('Batmobile lost a wheel')
print(mo.group(0))
print(mo.group(1))

# findall()
phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
fa = phone_num_regex.findall('Cell: 415-555-9999 Work,233-344,211, 212-555-0000')
print(fa)