import os

def path_filtr():
    list_f = []
    path = 'C:\Reposytory\PyEx2_3'
    for dirs, folder, fi in os.walk(path):
        for id_f in fi:
            if id_f.endswith('.txt'):
                list_f.append(id_f)
    return list_f

def len_list_f (list_file):
    len_f = len(list_file)
    return len_f

def length_file(list_f):
    dict = {}
    list_f_2 = []
    for name_file in list_f:
        counte = 0
        with open(name_file, encoding='utf=8') as file_s:
            for line in file_s:
                counte += 1
        list_f_2.append(counte)
        dict[name_file] = counte
    return dict

def sorted_file(dict_f, len_f):
    dict_file = {}
    list_2 = []
    list_3 = []
    for key, value in dict_f.items():
        list_2.append(key)
        list_3.append(value)
    counte_while = len_f
    counte = 0
    while counte_while >= 0:
        for key, value in dict_f.items():
            if value >= counte:
                counte = value
                if value == counte:
                    dict_file[key] = value
                    counte_while -= 1

    #print(counte)
    #print(list_2)
    #print(list_3)
    print(dict_file)


list_file = path_filtr()
#print(list_file)
length_files = length_file(list_file)
#print (length_files)
len_f = len_list_f(list_file)
#print (len_f)

sort = sorted_file(length_files,len_f)
print(sort)
