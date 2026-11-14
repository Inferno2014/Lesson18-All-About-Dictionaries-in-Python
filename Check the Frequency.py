dict1 = {'Codingal':2,'is':2,'best':2,'for':2,'coding':1}
print(dict1)
a = 0
b = 0
for i in dict1:
    if dict1[i] == 2:
        a+=1
    elif dict1[i] == 1:
        b+=1
if a > b:
    print("There are more 2's than 1's")
elif a < b:
    print("There are more 1's than 2's")