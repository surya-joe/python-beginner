from cmath import pi
import os
a = os.path.join('a','b','c')
print(a)

from pathlib import Path
b = Path('a').joinpath('b').joinpath('c')
print(b)

c = Path('a')/'b'/'c'
print(c)

my_files = ['accounts.txt', 'details.csv', 'invite.docx']
home = Path.home()
for filename in my_files:
    print(home / filename)

from os import chdir
print(Path.cwd())

chdir('/home/ubuntu/Videos')
print(Path.cwd())

cwd = Path.cwd()
(cwd/'one').mkdir()