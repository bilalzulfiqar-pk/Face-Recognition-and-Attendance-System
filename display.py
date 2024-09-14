import os


def display():
    path = 'Images'
    class_names = []
    class_id = []
    my_list = os.listdir(path)               # To Get All the items name (with Extension) inside that path Folder
    # print(my_list)
    try:
        for names in my_list:
            # print(names)
            class_id.append(names.split('.')[0])             # Appends ID in 'class_id'
            class_names.append(names.split('.')[1])          # Appends Name in 'class_names'
    except:
        print('Error....')
        print('Error in Splitting Image Names....\nCheck Image File Names in Image Folder')
        print('Also Note that there should not be any other File/Folder in Images Folder.')
        print('Check the Folder and run again...')
        exit()

    print('List of Stored Persons:')
    print('\nID\t\t\tName')

    for Id, Names in zip(class_id, class_names):                # Displaying Stored Persons
        print(Id + '\t\t' + Names)
    print('')
