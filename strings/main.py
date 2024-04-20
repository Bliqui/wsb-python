
def func_one(string):
    return len(string)

def func_two(string):
    letters = {}
    chars_arr = list(string)

    for char in chars_arr:
        if char in letters:
            letters[char] += 1
        else:
            letters.update({char: 1})
    
    return letters

def func_three(string):
    if len(string) < 2:
        return ""

    return string[0] + string[1] + string[-2] + string[-1]

def func_four(string):
    replacer = '$'
    if len(string) < 2:
        print('At least two characters is required')
        return string

    first_char = string[0]
    string_list = list(string)

    for index, char in enumerate(string_list[1:], start=1):
        if char == first_char:
            string_list[index] = replacer

    return ''.join(string_list)

def func_five(string1, string2):
        if len(string1) < 2 or len(string2) < 2:
            return "Both strings must have at least two characters."

        new_str1 = string2[:2] + string1[2:]
        new_str2 = string1[:2] + string2[2:]

        return new_str1 + ' ' + new_str2

def func_six(string):

    if len(string) < 3:
        return string
    if string.endswith('ing'):
        return string + 'ly'
    return string + 'ing'

def func_six(words_list):
    longest = max(words_list, key=len)
    return longest, len(longest)

def func_seven(string):
    if len(string) > 1:
        return string[-1] + string[1:-1] + string[0]
    return string

def func_eight(string):
    return string[::2]

def func_nine(string):
    words = {}
    words_arr = string.split(' ')

    for word in words_arr:
        if word in words:
            words[word] += 1
        else:
            words.update({word: 1})

    return words

def func_ten():
    user_input = input("Enter something: ")
    print(user_input.upper())
    print(user_input.lower())

def func_eleven(string):
    words = sorted(string.split(', '))
    return ', '.join(words)

def func_twelve(tag, word):
    return f'<{tag}>{word}</{tag}>'

def func_thirteen(wrapper, word):
    mid_of_wrapper = len(wrapper) // 2
    return wrapper[:mid_of_wrapper] + word + wrapper[mid_of_wrapper:]

def func_fourteen(string):
    if len(string) >= 2:
        return string[-2:] * 4
    return ''

def func_fifteen(string):
    if len(string) >= 3:
        return string[:3]
    else:
        return string

def func_sixteen(string):
    if (len(string) % 4 == 0):
        return string[::-1]
    else:
        return string

def func_seventeen(string):
    return string.replace('\n', '')

def func_eighteen(string):
    return string.swapcase()

def func_nineteen(string):
    return string.replace(' ', '')

def func_twentieth(string):
    return string.splitlines()
