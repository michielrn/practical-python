Python 3.9.7 (default, Sep 16 2021, 08:50:36) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.getcwd()
'/Users/michiel/practical-python/Work'
>>> with open('Data/portfolio.csv', 'rt') as f:
	data = f.read()

	
>>> data
'name,shares,price\n"AA",100,32.20\n"IBM",50,91.10\n"CAT",150,83.44\n"MSFT",200,51.23\n"GE",95,40.37\n"MSFT",50,65.10\n"IBM",100,70.44\n'
>>> print(data)
name,shares,price
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44

>>> with open('Data/portfolio.csv', 'rt') as f:
	for line in f:
		print(line, end = '')

		
name,shares,price
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44
>>> f = open('Data/portfolio.csv', 'rt')
>>> headers = next(f)
>>> headers
'name,shares,price\n'
>>> for line in f:
	print (line, end = '')

	
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44
>>> f.close()
>>> f=open('Data/portfolio.csv', 'rt')
>>> headers = next.split(',')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    headers = next.split(',')
AttributeError: 'builtin_function_or_method' object has no attribute 'split'
>>> headers = next(f).split(',')
>>> headers
['name', 'shares', 'price\n']
>>> for line in f:
	row = line.split(',')
	print(row)

	
['"AA"', '100', '32.20\n']
['"IBM"', '50', '91.10\n']
['"CAT"', '150', '83.44\n']
['"MSFT"', '200', '51.23\n']
['"GE"', '95', '40.37\n']
['"MSFT"', '50', '65.10\n']
['"IBM"', '100', '70.44\n']
>>> f.close()
>>> import gzip
>>> with gzip.open('Data/portfolio.csv.gz', 'rt') as f:
	for line in f:
		print(line, end = '')

		
name,shares,price
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44
>>> 