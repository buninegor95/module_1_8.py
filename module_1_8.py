my_dict = {'bobre': 666666666, 'neger': 888888888}
print('my_dict:', my_dict)
print('Existing value:', my_dict.get('neger'))
print('Deleted value:', my_dict.get('bomge'))
my_dict.update({"strelka" : 6573876734})
my_dict['belka'] = 9186545786
a = my_dict.pop('neger')
print('удалён',a)
print('Modified dictionary:', my_dict)


my_set = {6, 9, 3, 7, 6, 7, 3, 9, 42.314 ,'петух','блатной','петух', }
my_set.add(5)
my_set.add(10)
my_set.discard('петух')
print(set(my_set))




