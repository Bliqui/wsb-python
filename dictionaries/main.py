def func_first(dictionary, key, value):
    dictionary.update({key: value})

    return dictionary


def func_second(dicts_arr):
    merged_dicts = {}

    for dictionary in dicts_arr:
        merged_dicts.update(dictionary)

    return merged_dicts


def func_third(dictionary, key):
    return key in dictionary


def func_fourth(dictionary):
    for key, value in dictionary.items():
        print(key, value)


def func_fifth(n):
    result = {}

    for i in range(1, n + 1):
        result.update({i: i * i})

    return result


def func_sixth(n):
    result = {}

    for i in range(1, n + 1):
        result.update({i: i * i})

    return result


def func_seventh(dictionary1, dictionary2):
    merged = {}

    merged.update(dictionary1)
    merged.update(dictionary2)

    return merged


# def func_eighth(d):
#     for key, value in d.items():
#         print(key, value)


def func_eighth(dictionary):
    return sum(dictionary.values())


def func_ninth(dictionary):
    result = 1

    for value in dictionary.values():
        result *= value
    return result


def func_tenth(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return dictionary
    else:
        print('Key not found in dictionary')
        return dictionary


def func_eleventh(keys_list, values_list):
    return dict(zip(keys_list, values_list))


def func_twelfth(dictionary):
    return dict(sorted(dictionary.items()))


def func_thirteenth(dictionary):
    max_value = max(dictionary.values())
    min_value = min(dictionary.values())
    return max_value, min_value


def func_fourteenth(dictionary):
    return not bool(dictionary)


def func_fiveteenth(d1, d2):
    result = {}

    for key, value in d1.items():
        if key in d2:
            result[key] = value + d2[key]
        else:
            result[key] = value

    for key, value in d2.items():
        if key not in result:
            result[key] = value

    return result


def func_sixteenth(parent_keys, nested_keys, scores):
    nested_dict = []

    for i in range(len(parent_keys)):
        inner_dict = {nested_keys[i]: scores[i]}
        outer_dict = {parent_keys[i]: inner_dict}

        nested_dict.append(outer_dict)
    return nested_dict


def func_seventeenth(dictionary, value):
    only_booleans = []

    for key, item_value in dictionary.items():
        only_booleans.append(item_value == value)

    return all(only_booleans)


def func_eighteenth(dictionary):
    max_key = max(dictionary, key=dictionary.get)
    min_key = min(dictionary, key=dictionary.get)

    return (max_key, min_key)


def func_nineteenth(dictionary):
    return list(dictionary.values())


def func_twentieth(dictionary):
    return list(dictionary.keys())
