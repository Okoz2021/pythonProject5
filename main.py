import os

os.chdir(r'C:\\Users\\okoz2\\PycharmProjects\\pythonProject5\\sorted')
from pprint import pprint

files = os.listdir(path=r'C:\\Users\\okoz2\\PycharmProjects\\pythonProject5\\sorted')


def record_strings():
    dict_files = {}
    for name_file in files:
        with open(name_file, 'r', encoding='utf-8') as file:
            count_strings = file.readlines()
            myString = ' '.join(count_strings)
            item_list = dict({name_file: (len(count_strings), myString)})
            dict_files.update({name_file: (len(count_strings), myString)})
        dict_files.update(item_list)
        sorted_dict = sorted(dict_files.items(), key=lambda item: item[1])
    return sorted_dict


pprint(record_strings())


