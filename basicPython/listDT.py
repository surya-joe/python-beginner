spam = ['one','two','three','four']
spam2 = spam[:]
spam.append('five')
print(spam)
print(spam2)
print(len(spam))
spam[0] = 'zero'
print(spam)
print([1,2,3]+['A','B','C'])
print([1,2,3]*2)
