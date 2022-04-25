Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import urllib.request
u = urllib.request.urlopen('http://www.python.org/')
data = u.read()
data

int('N/A')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int('N/A')
ValueError: invalid literal for int() with base 10: 'N/A'
raise RuntimeError('What a Kerfuffle')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    raise RuntimeError('What a Kerfuffle')
RuntimeError: What a Kerfuffle
def greeting(name):
    '''
    Prints a simple greeting
    '''
    print('Hello', name)

    
greeting(Guido)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    greeting(Guido)
NameError: name 'Guido' is not defined
greeting('Guido')
Hello Guido
greeting('Michiel')
Hello Michiel
import csv
f=open('Data/portfolio.csv')
rows = csv.reader(f)
headers = next(rows)
headers
['name', 'shares', 'price']
for row in rows:
    print(row)

    
['AA', '100', '32.20']
['IBM', '50', '91.10']
['CAT', '150', '83.44']
['MSFT', '200', '51.23']
['GE', '95', '40.37']
['MSFT', '50', '65.10']
['IBM', '100', '70.44']
s = 'ABCD'
s[::-1]
'DCBA'
s = [1,2,3,4,5]
s[::-1]
[5, 4, 3, 2, 1]
f.close
<built-in method close of _io.TextIOWrapper object at 0x107d69490>
f.close()
