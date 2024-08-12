my_dict = {'Dzhamil': 1999, 'Eva': 1989, 'Sam': 1997, 'Ramilya': 1997}
print(my_dict)
print(my_dict['Eva'])
print(my_dict.get('Vlad'))
my_dict.update({'Kolya': 1998, 'Guzel': 1978})
print(my_dict.pop('Sam'))
print(my_dict)

my_set = {1, 2, 1, True, 2.0, 'Eva', True, 'Eva'}
print(my_set)  # Почему не выводится True и 2.0?
my_set.update(['Sam', (4, 1, 5)])
my_set.discard(1)
print(my_set)
