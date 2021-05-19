
def thesaurus(*args):
    result_dict = {}
    for name in sorted(args):
        result_dict.setdefault(name[0], []).append(name)
    return result_dict


def thesaurus_adv(*args):
    result_dict = {}
    for key_ln in sorted(list(set([full_name.split(' ')[1][0] for full_name in args]))):
        for key_fn in sorted(list(set([full_name.split(' ')[0][0] for
                                       full_name in
                                       sorted(list(filter(lambda full_name:
                                                          full_name.split(' ')[1].startswith(key_ln),
                                                          args)))]))):
            result_dict.setdefault(key_ln, {})[key_fn] = list(
                filter(lambda full_name: full_name.split(' ')[0].startswith(key_fn),
                       sorted(list(filter(lambda full_name:
                                          full_name.split(' ')[1].startswith(key_ln),
                                          args)))))
    return result_dict


def thesaurus_adv_ext(*args):
    result_dict = {}

    for full_name in sorted(args):
        result_dict.setdefault(full_name.split(' ')[1][0], {}).\
            setdefault(full_name.split(' ')[0][0], []).append(full_name)

    result_dict = dict(sorted(result_dict.items()))
    return result_dict


if __name__ == '__main__':
    names = thesaurus("Илья", "Иван", "Михаил", "Мария", "Петр")
    print("thesaurus")
    print(names)
    print("\r")

    names_adv = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
    print("thesaurus_adv")
    print(names_adv)
    print("\r")

    names_adv_ext = thesaurus_adv_ext("Инна Серова", "Петр Алексеев", "Илья Иванов", "Иван Сергеев", "Анна Савельева")
    print("thesaurus_adv_ext")
    print(names_adv_ext)
