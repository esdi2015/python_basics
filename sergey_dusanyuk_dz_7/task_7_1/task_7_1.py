import os
import shutil


project_structure = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}


def create_file(path_file):
    created_file = open(path_file, 'w+', encoding='utf-8')
    created_file.close()


def create_folder(path_folder):
    os.mkdir(path_folder)


def if_file_path(path_file):
    file_name = (path_file.split('/'))
    file_name.reverse()
    return True if len(file_name[0].split('.')) > 1 else False


def list_to_file_objects(file_objects_list, working_path='', paths_list=[]):
    for file_object in file_objects_list:
        if isinstance(file_object, str):
            file_object_path = os.path.join(working_path, file_object)
            paths_list.append(file_object_path)
        elif isinstance(file_object, dict):
            file_object_path = os.path.join(working_path, list(file_object.keys())[0])
            paths_list.append(file_object_path)
            paths_list = list_to_file_objects(list(file_object.values())[0], file_object_path, paths_list)
    return paths_list


if __name__ == '__main__':
    root_folder = os.path.dirname(os.path.abspath(__file__))

    for project_folder, obj in project_structure.items():

        if os.path.exists(os.path.join(root_folder, project_folder)):
            print('exists, remove [Y/n]')
            do_remove = input()
            if do_remove.lower() == 'n':
                exit(1)
            else:
                shutil.rmtree(os.path.join(root_folder, project_folder))

        os.mkdir(os.path.join(root_folder, project_folder))

        paths_ = list_to_file_objects(obj, os.path.join(root_folder, project_folder))

        for p in paths_:
            if if_file_path(p):
                create_file(p)
            else:
                create_folder(p)
