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
    for name_file in list_f:
        counte = 0
        with open(name_file, encoding='utf=8') as file_s:
            for line in file_s:
                counte += 1
        dict[counte] = name_file
    list1 = []
    for k in dict:
        list1.append(k)
        list1.sort()
    dict2 = {}
    for num in range(len(list1)):
        count = len(list1)
        while count >= 0:
            for ke, val in dict.items():
                if list1[num] == ke:
                    dict2[ke] = val
                    count -= 1
    return dict2

def read_files (dict):
    list_2 = []
    for key, value in dict.items():
        list_2.append(value)
        list_2.append(str(key))
        with open(value, encoding='utf=8') as file_s:
            for line in file_s:
                list_2.append(line)
    return list_2



list_file = path_filtr()
#print(list_file)
length_files = length_file(list_file)
#print (length_files)
len_f = len_list_f(list_file)
reads_files = read_files(length_files)
print(reads_files)
#print (len_f)
