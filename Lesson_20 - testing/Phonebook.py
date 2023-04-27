import json
import sys
import os.path
file_name = 'Phonebook.json'

def start():
    while True:
        a = input('Press 1 to update information, Press 2 to delete entry, Press 3 to search information, '
                  'Press 4 to add new entry, Press 5 to exit: ')
        if a != '1' and a != '2' and a != '3' and a != '4' and a != '5':
            print('Please choose number from 1 to 5')
            continue
        if a == '4':
            new_entry()
        if a == '5':
            exit()
        if a == '2':
            delete_entry()
        if a == '1':
            update_entry()
        if a == '3':
            search()

def update_entry():
    update_data = input('Input phone number for updating: ')
    with open(file_name, 'r+') as file_2:
        data = json.load(file_2)
        for txt in data['phonebook']:
            if txt['telephone number'] == update_data:
                n = input('Input name to update:')
                txt['name'] = n
                l_n = input('Input last name to update:')
                txt['last name'] = l_n
                txt['full name'] = n+' '+l_n
                txt['city'] = input('Input city to update:')
        with open(file_name, 'w') as out:
            json.dump(data, out, indent=4)
            print(data)

def new_entry():
    a = input('Input phone number to add: ')
    b = input('Input name to add:')
    c = input('Input last name to add:')
    d = input('Input city to add:')
    new_list = {'telephone number': a, 'name': b, 'last name': c, 'full name': b + ' ' + c, 'city': d}
    with open(file_name, 'r') as in_file:
        my_list = json.load(in_file)
        my_list['phonebook'].append(new_list)
        with open(file_name, 'w') as out:
            json.dump(my_list, out)
            print(my_list)

def exit():
    sys.exit()

def delete_entry():
    del_number = input('Input phone number for deleting: ')
    with open(file_name, 'r+') as file_2:
        data = json.load(file_2)
        i = 0
        for txt in data['phonebook']:
            if txt['telephone number'] == del_number:
                data['phonebook'].pop(i)
            i += 1
        with open(file_name, 'w') as out:
            json.dump(data, out)
            print(data)

def search():
    search_data = input('Input search parameter (telephone number, name, last name, full name or city): ')
    with open(file_name, 'r+') as file_2:
        data = json.load(file_2)
        i = 0
        for txt in data['phonebook']:
            if txt['telephone number'] == search_data:
                print(data['phonebook'][i])
            if txt['name'] == search_data:
                print(data['phonebook'][i])
            if txt['last name'] == search_data:
                print(data['phonebook'][i])
            if txt['full name'] == search_data:
                print(data['phonebook'][i])
            if txt['city'] == search_data:
                print(data['phonebook'][i])
        i += 1


# if __name__=='__main__':
#     file_name = 'Phonebook.json'
#     name, __ = os.path.splitext(file_name)
#     print(name)
#     print(sys.argv[0])
#     with open(file_name, 'r+') as file:
#         my_list = json.load(file)
#         print(my_list)
#         start()

