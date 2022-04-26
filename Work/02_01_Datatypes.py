Python 3.9.7 (default, Sep 16 2021, 08:50:36) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import csv
>>> f=read('Data/portfolio.csv')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    f=read('Data/portfolio.csv')
NameError: name 'read' is not defined
>>> f=open('Data/portfolio.csv')
>>> rows = csv.reader(f)
>>> next(rows)
['name', 'shares', 'price']
>>> row
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    row
NameError: name 'row' is not defined
>>> row = next(rows)
>>> row
['AA', '100', '32.20']
>>> t=(row[0], int(row[1]), float(row[2]))
>>> t
('AA', 100, 32.2)
>>> cost = t[1]*t[2]
>>> cost
3220.0000000000005
>>> print(f'{cost:0.2f}')
3220.00
>>> t[2]=75.0
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    t[2]=75.0
TypeError: 'tuple' object does not support item assignment
>>> t=t[0],75,t[2]
>>> t
('AA', 75, 32.2)
>>> name,share, price = t
>>> name
'AA'
>>> share
75
>>> price
32.2
>>> t=name, share, price
>>> t
('AA', 75, 32.2)
>>> t=name, 2*share, price
>>> t
('AA', 150, 32.2)
>>> d={
	'name': row[0],
	'share': row[1],
	'price': row[2]
	}
>>> d
{'name': 'AA', 'share': '100', 'price': '32.20'}
>>> d={
	'name': row[0],
	'share': int(row[1]),
	'price': float(row[2])
	}
>>> d
{'name': 'AA', 'share': 100, 'price': 32.2}
>>> cost = d['share']*d['price']
>>> cost
3220.0000000000005
>>> d['share']=75
>>> cost
3220.0000000000005
>>> cost = d['share']*d['price']
>>> cost
2415.0
>>> d['date']=(6,6,2007)
>>> d['account']=12345
>>> d
{'name': 'AA', 'share': 75, 'price': 32.2, 'date': (6, 6, 2007), 'account': 12345}
>>> for k in d:
	print(f'k = {k}')

	
k = name
k = share
k = price
k = date
k = account
>>> for k in d:
	print(f'{k} = {d[k]}')

	
name = AA
share = 75
price = 32.2
date = (6, 6, 2007)
account = 12345
>>> keys = d.keys()
>>> keys
dict_keys(['name', 'share', 'price', 'date', 'account'])
>>> del d['account']
>>> keys
dict_keys(['name', 'share', 'price', 'date'])
>>> items = d.items()
>>> items
dict_items([('name', 'AA'), ('share', 75), ('price', 32.2), ('date', (6, 6, 2007))])
>>> for k,v in items:
	print(f'{k}: {v}')

	
name: AA
share: 75
price: 32.2
date: (6, 6, 2007)
>>> items
dict_items([('name', 'AA'), ('share', 75), ('price', 32.2), ('date', (6, 6, 2007))])
>>> d = dict(items)
>>> d
{'name': 'AA', 'share': 75, 'price': 32.2, 'date': (6, 6, 2007)}
>>> 