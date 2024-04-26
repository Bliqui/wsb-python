import random

def func_first():
    result = []
    for number in range(1500, 2701):
        if number % 7 == 0 and number % 5 == 0:
            result.append(number)
    return result


def func_second(temp, convert_to):
    if convert_to.lower() == 'celsius':
        return (temp * 9/5) + 32
    elif convert_to.lower() == 'fahrenheit':
        return (temp - 32) * 5/9


def func_third(word):
    reversed_word = ''
    for char in reversed(word):
        reversed_word += char
    return reversed_word


def func_fourth(datalist):
    for item in datalist:
        print(f'Item: {item}, Type: {type(item)}')


def func_fifth():
    for num in range(7):
        if num in [3, 6]:
            continue
        print(num, end=' ')


def func_sixth():
    int_to_guess = random.randint(1, 9)
    int_guessed = False
    
    while not int_guessed:
      user_input = input("Guess the number: ")
      
      if int(user_input) == int_to_guess:
        int_guessed = True
    
    return print("Well guessed!")
  

def func_seventh(finish):
    for i in range(finish):
        print('*' * i)
    for j in range(finish, 0, -1):
        print('*' * j)
        

def func_eigth(start, end):
    if start < 1:
      print("Start arg can't be smaller than 1")
      return ''
    
    result = ''

    for i in range(start, end + 1):
      if i % 3 == 0:
        result += 'Fizz'
      if i % 5 == 0:
        result += 'Buzz'
      
      if result:
        print(result)
        result = ''
      else:
        print(i)
        
  
def func_tenth():
    while True:
      provided_string = input()
      
      if (provided_string):
        print(provided_string.lower())
      else:
        break
  
  
def func_eleventh(string):
    ints = 0
    letters = 0
    
    for symbol in string:
      if symbol.isdigit():
        ints += 1
      elif symbol.isalpha():
        letters += 1
    
    print(f'Letters {letters}')
    print(f'Digits {ints}')
    
def func_twelfth(password):
    if not (6 <= len(password) <= 16):
        print("Password is invalid.")
        print("Password must be between 6 and 16 characters.")
        return False

    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    for char in password:
      if char.isdigit():
          has_digit = True
      elif char.islower():
          has_lower = True
      elif char.isupper():
          has_upper = True
      elif char in ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']:
          has_special = True
          
    is_valid_password = has_lower and has_upper and has_digit and has_special

    if not is_valid_password:
        print("Password is invalid.")
        print("Make sure your password includes at least one lowercase letter, one uppercase letter, one digit, and one special character")
        
        return False
    else:
        print("Password is valid.")
        return True


def func_thirteenth():
    results = []
    
    for number in range(100, 401):
        number_str = str(number)
        
        if all(int(digit) % 2 == 0 for digit in number_str):
            results.append(number_str)

    print(", ".join(results))

def func_fourtheenth(age_in_human_years):
    if age_in_human_years < 0:
        print("Age must be positive number.")
        return 0
    
    if age_in_human_years <= 2:
        dog_years = age_in_human_years * 10.5
    else:
        dog_years = 21 + (age_in_human_years - 2) * 4
    
    return dog_years


def func_fifteenth(letter):
    vowels = 'aeiou'
    
    if len(letter) != 1 or not letter.isalpha():
        print("Please enter a single alphabet character.")
    else:
        if letter.lower() in vowels:
            print(f"{letter} is a vowel.")
        else:
            print(f"{letter} is a consonant.")


def func_sixteenth(month):
    month_days = {
        "january": "31", "february": "28/29", "march": "31",
        "april": "30", "may": "31", "june": "30",
        "july": "31", "august": "31", "september": "30",
        "october": "31", "november": "30", "december": "31"
    }
    
    if month.lower() in month_days:
        print(f"Number of days: {month_days[month.lower()]} days")
    else:
        print("Wrong month name")

def func_seventeenth(first, second):
    sum = first + second
    
    if 15 <= sum <= 20:
        return 20
    else:
        return sum

def func_eighteenth(symbol):
    if isinstance(symbol, int):
        return True
    
    return False

def func_nineteenth(first, second, third):
    grouped_digits = [first, second, third]
  
    if any(not isinstance(x, int) and not isinstance(x, float) for x in grouped_digits):
      print('Only didgits are accepted.')
      return 0

    sorted_digits = sorted(grouped_digits)
    
    median = sorted_digits[1]
    
    print(f'The median is {median}')
    
    return median
  

def func_twentieth(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

