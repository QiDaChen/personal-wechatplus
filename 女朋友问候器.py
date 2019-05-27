with open('qinghua.txt','r') as file:
    a = file.read()
a = a.split('\n')
for i in a:
    print(i)