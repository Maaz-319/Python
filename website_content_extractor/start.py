from urllib.request import urlopen
from random import randint

filename = "data{0}.txt".format(str(randint(1, 10000000)))
file1 = open(filename, 'w')
page = input('Enter link: ')
open = urlopen(page)

content = str(open.read())

file1.write(content)
file1.close()
print(filename + ' file has been created!')
input()
