import os


def delete_record(id, name):
    path = 'Images'
    my_list = os.listdir(path)  # To Get All the items name (with Extension) inside that path Folder
    # print(my_list)
    if not id:
        print('At Least ID Field is Required')
    else:
        if not name:  # executes if the user entered only in ID Field and name field is empty
            delete_file_by_id(id, my_list, path)
        else:  # executes if the user entered both in ID Field and name Field
            delete_file_by_id_and_name(id, name, path)
    print('')


def delete_file_by_id(id, my_list, path):
    found = False  # comment about is at line 81
    for name in my_list:
        if name.split('.')[0] == id:  # Split the ID from Full File Name and Compare it with Given ID
            os.remove(f'{path}/{name}')  # removes Image File
            print(f'File {name} Deleted Successfully.')
            found = True
            break
    if not found:  # executes if the found is False which means File has not found
        print(f'File with ID: {id} does not exist')


def delete_file_by_id_and_name(id, name, path):
    if os.path.exists(f'{path}/{id}.{name}.jpg'):  # check if the File Exists
        os.remove(f'{path}/{id}.{name}.jpg')  # removes Image File
        print(f'File {id}.{name}.jpg Deleted Successfully.')
    else:
        print(f'File {id}.{name}.jpg does not exist')
