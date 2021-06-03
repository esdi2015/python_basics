import os

explore_dir = '/etc/'

cnt = dict()
ext = dict()

for root, dirs, files in os.walk(explore_dir):
    for file in files:
        key = 10**(len(str(os.stat(os.path.join(root, file)).st_size)))
        cnt[key] = cnt.get(key, 0) + 1
        file_ext = file.split('.')[-1] if len(file.split('.')) > 1 else 'No Extension'
        if key in ext:
            ext[key].add(file_ext)
        else:
            ext[key] = set()
            ext[key].add(file_ext)

res_dict = {k: (v, list(ext[k])) for k, v in cnt.items()}
res_dict = dict(sorted(res_dict.items(), key=lambda item: item[0]))

print(res_dict)
