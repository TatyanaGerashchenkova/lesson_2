my_list = [25, -25, 2.5, None, 'None', 'Hello', (2,5), {1: 300, 2: 'Max'}]
for i, item in enumerate(my_list, 1):
    print(f'{i}) {item} - {type(item)}')