
def file_data(file):
    with open(file, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f]


if __name__ == '__main__':
    users_file = 'users.csv'
    hobby_file = 'hobby.csv'

    users_data = file_data(users_file)
    hobby_data = file_data(hobby_file)

    users_data_len = len(users_data)
    hobby_data_len = len(hobby_data)

    if users_data_len < hobby_data_len:
        exit(1)

    if users_data_len > hobby_data_len:
        ext_none = [None for i in range(0, users_data_len-hobby_data_len)]
        hobby_data.extend(ext_none)

    res_dict = dict(zip(users_data, hobby_data))

    print(res_dict)



