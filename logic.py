"""Program for converting Arabic numbers to Roman Numerals
   Author: Peter J Scriven
   Started: 8th June 2014
   Updated: 12th June 2014
   """


def number_to_numeral(number):
    value_list = [('M', 1000), ('CM', 900), 
                  ('D', 500), ('CD', 400), 
                  ('C', 100), ('XC', 90), 
                  ('L', 50), ('XL', 40),
                  ('X', 10), ('IX', 9), 
                  ('V', 5), ('IV', 4), 
                  ('I', 1)]
    count_dict = {'M': 0, 'CM': 0, 'D': 0, 'CD': 0, 'C': 0, 'XC': 0,
                  'L': 0, 'XL': 0, 'X': 0, 'IX': 0, 'V': 0, 'IV': 0, 'I': 0}
    for key, value in value_list:
        count_dict[key] = number // value
        number = number % value
    char_list = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    num_list = []
    for char in char_list:
        count = count_dict[char]
        num_list.append(char * count)
    numeral = ''
    for i in num_list:
        numeral += i
    return numeral


def numeral_to_number(numeral):
    value_dict = {'M': 1000,
                  'D': 500,
                  'C': 100,
                  'L': 50,
                  'X': 10,
                  'V': 5,
                  'I': 1}
    letter_list = list(numeral)
    letter_list.reverse()
    number = 0
    if len(numeral) > 0:
        current_letter = letter_list[0]
        for letter in letter_list:
            if value_dict[letter] >= value_dict[current_letter]:
                number += value_dict[letter]
                current_letter = letter
            else:
                number -= value_dict[letter]
    return number


def is_valid_numeral(text):
    valid_chars = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    
    valid = True
    if type(text) == str:
        for letter in list(text):
            if letter not in valid_chars:
                # print(letter)
                valid = False
    
    else:
        valid = False
    return valid


def is_valid_number(text):
    return text.isnumeric()


# ---- If you just want to use this is the python shell ----
TEXT_MODE = False


def get_number():
    not_received_number = True
    while not_received_number:
        try:
            num = int(input("\nPlease input your number: "))
            not_received_number = False
        except:
            print("That is not a number")
        else:
            if num > 100000000000000:
                print("Okay, now this is just getting ridiculous.")
                not_received_number = True
            elif num > 1000000000:
                print("Seriously, if I let you do this your computer would take like a minute just to calculate it.")
                not_received_number = True
            elif num > 100000000:
                print("Nope. Numerals for numbers over 100 million just get stupidly big.")
                not_received_number = True
            elif num > 100000:
                print("Your numeral would contain {} M's".format(number // 1000))
                not_received_number = True
    return num


while TEXT_MODE:
    number = get_number()
    numeral = number_to_numeral(number)
    print("Your numeral is: " + numeral)
