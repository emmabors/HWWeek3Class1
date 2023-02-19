import re
with open('regex_test (1).txt') as my_file:
    data = my_file.readlines()
    for name in data:
        pattern = re.compile(r'[A-Za-z]+[" "][A-Z][a-zA-Z]+')
        match = pattern.findall(name)
        if match:
            print(name)
        else:
            print(None)



