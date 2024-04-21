def func_first(items):
    return sum(items)


# print(func_first([1, 2, 3]))

def func_second(items):
    result = 1
    for i in items:
        result *= i
    return result


# print(func_second([1, 2, 3, 4]))

def func_third(items):
    return max(items)


# print(func_third([1, 2, 3]))

def func_fourth(items):
    return min(items)


def func_fifth(items):
    count = 0

    for item in items:
        if len(item) > 2 and item[0].lower() == item[-1].lower():
            count += 1

    return count


def func_sixth(list1, list2):
    new_arr = []

    new_arr.extend(list1)
    new_arr.extend(list2)

    return new_arr


def func_seventh(items):
    return list(set(items))


def func_eighth(items):
    return len(items) > 0


def func_ninth(items):
    return items.copy()


def func_tenth(n, items):
    longer_words = []

    for item in items:
        if len(item) > n:
            longer_words.append(item)

    return longer_words


def func_eleventh(list1, list2):
    hasCommonChar = False

    for i in list1:
        for j in list2:
            if i == j:
                hasCommonChar = True

    return hasCommonChar


def func_twelfth(list):
    new_arr = []

    for idx, i in enumerate(list):
        if idx != 0 and idx != 4 and idx != 5:
            new_arr.append(i)

    return new_arr


def func_thirteenth(list):
    if len(list) < 2:
        print('At lest 2 elements list')
        return list

    sorted_list = sorted(list)

    return sorted_list[1]


def func_fourteenth(list):
    filtered_list = []

    for i in list:
        if i % 2 != 0:
            filtered_list.append(i)

    return filtered_list


def func_fifteenth(list):
    if len(list) < 2:
        print('At lest 2 elements list')
        return list

    sorted_list = sorted(list)

    return sorted_list[-2]


def func_sixteenth(list):
    frequency = {}

    for i in list:
        if i not in frequency:
            frequency[i] = 1
        else:
            frequency[i] += 1

    return frequency


def func_seventeenth(list):
    result = ""

    for i in list:
        result += str(i)

    return result


def func_eighteenth(list):
    filtered_arr = []

    for i in list:
        if i % 2 != 0:
            filtered_arr.append(i)

    return filtered_arr


def func_nineteenth(symbol, list):
    if len(list) < 1:
        print('At lest 2 elements list')
        return list

    modified_arr = []

    for item in list:
        modified_arr.append(symbol)
        modified_arr.append(item)

    return modified_arr


def func_twentieth(list1, list2):
    new_arr = []

    if len(list1) == 0:
        return list2

    for idx, i in enumerate(list1):
        if idx != len(list1) - 1:
            new_arr.append(i)
        else:
            for j in list2:
                new_arr.append(j)

    return new_arr
