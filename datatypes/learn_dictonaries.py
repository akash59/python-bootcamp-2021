# dictionaries can not be sorted
my_dict = {'key1': 'value1', 'key2': 'value2'}
print(my_dict['key1'])

prices_lookup = {'apple': '2.99', 'oranges': 1.99, 'milk': 5.80}
print(prices_lookup['apple'])

d = {'k1': 123, 'k2': [0, 1, 'c'], 'k3': {'insideKey': 100}}
print(d['k2'])
print(d['k3']['insideKey'])
letter = (d['k2'][2]).upper()
print(letter)

prices_lookup['coffee'] = 10.19
prices_lookup['milk'] = 5.86

print(prices_lookup)

# dict methods
print(d.keys())
print(d.values())
print(d.items()) # returns a list of tuples

# checked ordered dict functionality later for ordered items in dict.




