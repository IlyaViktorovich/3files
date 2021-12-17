import os

def path_filtr ():
    list_f = []
    path = 'C:\Reposytory\PyEx2_3'
    for dirs,folder,fi in os.walk(path):
        for id_f in fi:
            if id_f.endswith('.txt'):
                list_f.append(id_f)
    return list_f

def read_txt (list_f):
    path = 'C:\Reposytory\PyEx2_3'
    for id_f in list_f:
        print(id_f)
        counte = 0
        with open(id_f) as file_1:
            for line in file_1:
                print(line)
    #cook_recipe = []
    #with open(file_name) as file:
        #for line in file:
            #cook_recipe.append(line.strip())
            #number_recipe = int(file.readline().strip())
            #for ingredients in range(number_recipe):
                #print(file.readline())
            #file.readline()


list_file = path_filtr ()
print(list_file)
print (read_txt (list_file))
