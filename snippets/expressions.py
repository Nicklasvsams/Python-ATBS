print((5 > 4) and (3 == 5)) #False
print(not (5 > 4)) #False
print((5 > 4) or (3 == 5)) #True
print(not ((5 > 4) or (3 == 5))) #False
print((True and True) and (True == False)) #False
print((not False) or (not True)) #True

for i in range(1, 11):
    print(i)

i = 1

while(i < 11):
    print(i)
    i = i + 1