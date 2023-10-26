# task 2

dict = {}
dict.values()

while True:
    name = input('enter the person is  name>>')
    if name == 'stop':
        break
    age = input('enter the user is age>>')

    dict[name] = int(age)
    print(dict)

    max_age = 0
    max_name = ''
    for i in dict.keys():
        if int(dict[i]) > max_age:
            max_name = i
            max_age = dict[i]
print(max_age, max_name)
    