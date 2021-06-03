import os

explore_dir = '/etc/'

res_dict = dict()

for root, dirs, files in os.walk(explore_dir):
    for file in files:
        key = 10**(len(str(os.stat(os.path.join(root, file)).st_size))+1)
        res_dict[key] = res_dict.get(key, 0) + 1

res_dict = dict(sorted(res_dict.items(), key=lambda item: item[0]))

print(res_dict)

