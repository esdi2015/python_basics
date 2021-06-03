import os
import shutil
import json

structure_file_name = 'structure.json'

project_structure = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}


def get_structure_from_file(structure_file_path):
    with open(structure_file_path, 'r', encoding='utf-8') as f:
        lines = f.read()
    lines = lines.strip()
    return json.loads(lines)


def create_file(path_file):
    created_file = open(path_file, 'w+', encoding='utf-8')
    created_file.close()


def create_folder(path_folder):
    os.mkdir(path_folder)


def create_file_object(path_object):
    if if_file_path(path_object):
        create_file(path_object)
    else:
        create_folder(path_object)


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
    project_structure = get_structure_from_file(os.path.join(root_folder, structure_file_name))
    project_folder, project_file_objects = list(project_structure.keys())[0], list(project_structure.values())[0]

    if os.path.exists(os.path.join(root_folder, project_folder)):
        print('exists, remove [Y/n]')
        do_remove = input()
        if do_remove.lower() == 'n':
            exit(1)
        else:
            shutil.rmtree(os.path.join(root_folder, project_folder))

    os.mkdir(os.path.join(root_folder, project_folder))
    paths = list_to_file_objects(project_file_objects, os.path.join(root_folder, project_folder))

    for p in paths:
        create_file_object(p)

