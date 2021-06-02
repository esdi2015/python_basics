import os
import shutil
from os.path import relpath


project_structure = {'my_project': [{'settings': ['__init__.py', 'dev.py', 'prod.py']},
                                    {'mainapp': ['__init__.py', 'models.py', 'views.py',
                                                 {'templates': ['base.html', 'index.html']}]},
                                    {'authapp': ['__init__.py', 'models.py', 'views.py',
                                                 {'templates': ['base.html', 'index.html', 'config.ini']}]},
                                    {'tests': ['__init__.py', 'utils.py',
                                               {'helpers': ['__init__.py',
                                                            {'templates': ['base.html', 'index.html', 'styles.css']}]}]}
                                    ]}


def str_strip(str_):
    return str_.strip()


def get_structure_from_file(structure_file_path):
    struct_dict = {}
    with open(structure_file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines() # .readline()

    lines = map(str_strip, lines)
    print(lines)

    for line in lines:
        if len(line.split(' ')) > 1:
            item_level = len(line.split(' ')[0])
        else:
            item_level = 0
        # print(line)
        # print(line.split(' '))
        print(*(line, item_level), sep=' ::: ')

    # root_item = line.strip()
    # while line:
    #     line = f.readline().strip()
    #
    #     print(line)
    #     print(item_level)
    #     if len(line.split('.')) > 1:
    #         print('file')
    #     else:
    #         print('folder')

    return


def create_file(path_file):
    created_file = open(path_file, 'w+', encoding='utf-8')
    created_file.close()


def create_folder(path_folder):
    os.mkdir(path_folder)


def if_file_path(path_file):
    file_name = (path_file.split('/'))
    file_name.reverse()
    return True if len(file_name[0].split('.')) > 1 else False


def list_to_file_objects(file_objects_list, working_path='', paths_list=None):
    if paths_list is None:
        paths_list = []
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
    project_folder, project_file_objects = list(project_structure.keys())[0], list(project_structure.values())[0]

    print(os.path.join(root_folder, 'structure.txt'))

    get_structure_from_file(os.path.join(root_folder, 'structure.txt'))

    exit(0)

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
        if if_file_path(p):
            create_file(p)
        else:
            create_folder(p)

    root_dir = os.path.join(root_folder, project_folder)
    template_folder_name = 'templates'
    template_folder_path = os.path.join(root_dir, template_folder_name)
    template_file_ext = ('html', )
    templates_files = []

    for root, dirs, files in os.walk(root_dir):
        if root.split('/')[:-2:-1][0] == template_folder_name:
            for file in files:
                if file.rsplit('.', maxsplit=1)[-1].lower() in template_file_ext:
                    orig_file_path = os.path.join(root, file)
                    rel_path = relpath(orig_file_path, root_dir)
                    rel_path = rel_path.split('/')
                    rel_path.pop(rel_path.index(template_folder_name))
                    template_files_path = os.path.join(template_folder_path, '/'.join(rel_path))
                    templates_files.append((orig_file_path, template_files_path))

    create_folder(template_folder_path)

    for from_path, to_path in templates_files:
        os.makedirs(os.path.dirname(to_path), exist_ok=True)
        shutil.copy2(from_path, to_path)

