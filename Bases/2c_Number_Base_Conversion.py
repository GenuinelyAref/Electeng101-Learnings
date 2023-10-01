# program to change a number of any base to any other base (combines usage of 2a and 2b)
import math


# FUNCTIONS TO CONVERT FROM ANY BASE TO DECIMAL:
# function to retrieve subscript character unicode equivalent for any digit (0-9)
def special_num(var_num, var_type, var_sign):
    # define subscript unicode character lists
    if var_type == "sub":
        unicode_chars = ['\u2080', '\u2081', '\u2082', '\u2083', '\u2084',
                         '\u2085', '\u2086', '\u2087', '\u2088', '\u2089']
    # define superscript unicode character list
    else:
        unicode_chars = ['\u2070', '\u00b9', '\u00b2', '\u00b3', '\u2074',
                         '\u2075', '\u2076', '\u2077', '\u2078', '\u2079']
    negative_superscript = "\u207B"
    # define used variable
    special_text = ""
    # repeat for each digit in the number provided
    for i in range(0, len(str(var_num))):
        # convert each digit into its subscript unicode equivalent
        special_text += unicode_chars[int((str(var_num))[i])]
    if var_sign == "-":
        special_text = negative_superscript + special_text
    # return subscript unicode equivalent to caller (ready to print)
    return special_text


# write number with base in subscript
def write_number(var_num, var_base):
    # concatenate number with its base in subscript
    var_return_num = "{}{}".format(var_num, special_num(var_base, "sub", "+"))
    # return text output to caller
    return var_return_num


# expand a single digit using base and place-value
def expanded_term(var_digit, var_base, var_place_value, var_sign):
    # concatenate digit with base ^ place value
    var_expanded_term = "{}x{}{}".format(var_digit, var_base, special_num(var_place_value, "super", var_sign))
    # return text output to caller
    return var_expanded_term


# fully expand the number
def full_expansion(var_num, var_base):
    # define output variables
    expanded_text = ""
    expanded_terms = []
    # convert number into list, each character as a list item
    str_var_num = list(str(var_num))
    # check for a decimal point
    try:
        dot_index = str_var_num.index(".")
        # if one is found, then collect its index and remove it from list
        str_var_num.pop(dot_index)
    except ValueError:
        # otherwise set index to -1
        dot_index = -1
    # get number of characters in number
    var_digits = len(str_var_num)

    # if number has no decimal part
    if dot_index == -1:
        # go down each digit
        for digit_index in range(0, var_digits):
            # get power of base
            var_placeholder = var_digits - digit_index - 1
            # get digit from number
            var_digit = str_var_num[digit_index]
            # if it's not the last digit, add a "+" and <space> at the end
            if digit_index != var_digits - 1:
                # expand the digit out using base and place-value
                expanded_text += "{} + ".format(expanded_term(var_digit, var_base, var_placeholder, "+"))
            # otherwise no space or plus sign
            else:
                # expand the digit out using base and place-value
                expanded_text += "{}".format(expanded_term(var_digit, var_base, var_placeholder, "+"))
            # add each number (accounting for its place value) to list
            expanded_terms.append(int(var_digit) * (int(var_base) ** var_placeholder))

    # if number has a decimal point
    else:
        # go down each digit
        for digit_index in range(0, var_digits):
            # get power of base
            var_placeholder = dot_index - digit_index - 1
            # adjust negative powers to display correctly
            if var_placeholder < 0:
                var_sign = "-"
                var_placeholder_adjusted = var_placeholder * -1
            else:
                var_sign = "+"
                var_placeholder_adjusted = var_placeholder
            # get digit from number
            var_digit = str_var_num[digit_index]
            # if it's not the last digit, add a "+" and <space> at the end
            if digit_index != var_digits - 1:
                # expand the digit out using base and place-value
                expanded_text += "{} + ".format(expanded_term(var_digit, var_base, var_placeholder_adjusted, var_sign))
            # otherwise no space or plus sign
            else:
                # expand the digit out using base and place-value
                expanded_text += "{}".format(expanded_term(var_digit, var_base, var_placeholder_adjusted, var_sign))
            # add each number (accounting for its place value) to list
            expanded_terms.append(int(var_digit) * (int(var_base) ** var_placeholder))
    # return expanded form of number & all the expanded terms
    return [expanded_text, expanded_terms]


# get type of input (decimal or integer):
def get_type():
    valid_input = False
    # repeat until type input is valid
    while not valid_input:
        # get input from user
        var_num_type = input("Is your number a (1) decimal or an (2) integer? Enter the number here: ")
        # check if input is 1
        if var_num_type.strip(" ") == "1":
            return "decimal"
        # check if input is 2
        elif var_num_type.strip(" ") == "2":
            return "integer"
        # otherwise input is invalid
        else:
            # show error message
            print("\nPlease enter 1 or 2.\n")
            # repeat cycle
            valid_input = False


# get type of base 10 output (decimal or integer)
def get_type_no_input(var_value):
    # convert value into decimal (from string)
    var_value = float(var_value)
    # if value is an integer
    if var_value - int(var_value) == 0:
        return "integer"
    # otherwise, it must be a decimal
    else:
        return "decimal"


# get base value from user
def get_base(var_type):
    # assign prompt based on type of base being requested
    if var_type == "old":
        prompt = "What base is your number in? Enter a number (>1) here: "
    else:
        prompt = "What base do you want to convert into? Enter a number (>1) here: "
    base_valid = False
    # repeat until base input is valid
    while not base_valid:
        # get input from user
        var_base = input("\n{}".format(prompt))
        try:
            # see if input is a number
            x = int(var_base)
            # see if input is an integer bigger than 1
            condition_met = (x > 1) and (float(x) % 1 == 0)
            if condition_met:
                return x
            else:
                # print error message
                print("That's not a valid base, try again.\n")
                base_valid = False
        # if input is text / other non-integer
        except ValueError:
            # print error message
            print("That's not a valid base, try again.\n")
            base_valid = False


# write out the second expansion step (sum of all expanded terms)
def expansion_step_two(var_expanded_values):
    # define used variable
    var_expanded_text = ""
    # repeat for every expanded term
    for var_num in range(0, len(var_expanded_values)):
        # if it's not the last expanded term
        if var_num != (len(var_expanded_values) - 1):
            # add a plus at the end
            var_expanded_text += "{} + ".format(var_expanded_values[var_num])
        # otherwise, no plus sign at the end
        else:
            var_expanded_text += "{}".format(var_expanded_values[var_num])
    # return sum of all expanded terms as a text output
    return var_expanded_text


# FUNCTIONS TO CONVERT FROM ANY BASE BACK TO DECIMAL:
# check if user wants a custom alphabet
def check_custom_alphabet():
    # define affirmative and negative responses
    affirmative_responses = ['yes', 'y']
    negative_responses = ['no', 'n']
    # preset loop condition before getting an input
    valid_input = False
    # repeat until input is valid (either yes or no)
    while not valid_input:
        # get user input
        valid_input = input("\nWould you like to use a custom alphabet? Yes/no: ").lower()
        if valid_input in affirmative_responses:
            # if input matches any of the affirmative responses, return True
            return True
        elif valid_input in negative_responses:
            # if input matches any of the negative responses, return False
            return False
        else:
            # print error message & keep loop condition false
            print("Please enter yes/no.\n")
            valid_input = False


# get custom alphabet from user
def get_custom_alphabet(var_base):
    # give user instruction on entering characters
    print("Enter each character in your {}-character alphabet, one by one, pressing <enter> after each characters"
          .format(var_base))
    # define used variable
    var_custom_alphabet = []
    # repeat for each character in the alphabet
    for chars in range(0, var_base):
        # get each alphabet character one by one
        var_custom_alphabet.append(input("Character #{}: ".format(chars + 1)).strip(" "))
    # return list to caller
    return var_custom_alphabet


# convert integer part into new base
def convert_integer(var_int_part, var_new_base, var_alphabet):
    # define used variables
    var_converted_num = ""
    var_alphabet_indices = []
    # repeat until quotient is zero
    while var_int_part != 0:
        # calculate digits starting from least significant digit
        var_remainder = var_int_part % var_new_base
        # record index of character to call from alphabet at the end
        var_alphabet_indices.insert(0, var_remainder)
        # calculate 'carried-on' (quotient) integer value
        var_int_part = var_int_part // var_new_base
    # concatenate all digits by using the provided alphabet
    for char in range(0, len(var_alphabet_indices)):
        # call each character from the alphabet, one by one, and concatenate the base-converted number
        var_converted_num += var_alphabet[var_alphabet_indices[char]]
    # return base-converted number to use
    return var_converted_num


# convert fractional part into new base
def convert_fractional(var_fractional_part, var_new_base, var_alphabet):
    # define used variables
    var_converted_num = ""
    var_alphabet_indices = []
    # convert fractional part to an actual decimal (float)
    var_fractional_part = float("0.{}".format(str(var_fractional_part)))
    # repeat until fraction part is 0
    while var_fractional_part != 0:
        # calculate digits starting from least significant digit
        var_int_part = math.floor(var_fractional_part * var_new_base)
        # record index of character to call from alphabet at the end
        var_alphabet_indices.append(var_int_part)
        # calculate remaining fractional part
        var_fractional_part = (var_fractional_part * var_new_base) - var_int_part
    # concatenate all digits by using the provided alphabet
    for char in range(0, len(var_alphabet_indices)):
        # call each character from the alphabet, one by one, and concatenate the base-converted number
        var_converted_num += var_alphabet[var_alphabet_indices[char]]
    # return base-converted number to use
    return var_converted_num


# split decimal numbers (with decimal points) into integer and fractional parts
def split_decimals(var_number):
    # find location of decimal point
    var_point_index = list(str(var_number)).index(".")
    # find integer part of number
    var_integer_part = int(str(var_number)[0:var_point_index])
    # find fractional part of number
    var_fractional_part = int(str(var_number)[var_point_index + 1:])
    # return both parts separately
    return [var_integer_part, var_fractional_part]


# MAIN ROUTINE

# welcome message
print("Base conversion program\n\n")
# disclaimers
print("*uses hex alphabet for bases of 16 and under")
print("*bases bigger than 16 need custom alphabet\n\n")

# get type of input (decimal or integer number)
num_type = get_type()

# get number
number = input("\nEnter your number: ")

# assign suitable type to number
if num_type == "decimal":
    number = float(number)
else:
    number = int(number)

# get base value
old_base = get_base("old")

# get base value
new_base = get_base("new")

# if base is less than 16, give the option of a custom alphabet
if new_base <= 16:
    need_custom_alphabet = check_custom_alphabet()
# if base is bigger than 16, then the custom alphabet is compulsory
else:
    need_custom_alphabet = True

# get custom alphabet if required
if need_custom_alphabet:
    alphabet = get_custom_alphabet(new_base)
# otherwise, use hex alphabet by default (for bases <= 16)
else:
    alphabet = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

# number with base
number_label_base = write_number(number, old_base)
# get full expansion of number (convert into base-10 number)
expansion_raw = full_expansion(number, old_base)
# calculate spacing for left-aligned printing
spacer = " " * len(number_label_base)
# calculate the decimal base number
decimal_number = sum(expansion_raw[1])
# assign type of decimal number
decimal_type = get_type_no_input(decimal_number)

# write input number & base and full expansion to create text output
output_line_one = "{} = {}".format(number_label_base, expansion_raw[0])
# write sum of expanded terms to text output
output_line_two = "{} = {}".format(spacer, expansion_step_two(expansion_raw[1]))
# write actual sum of expanded terms (single term) to text output
output_line_three = "{} = {}".format(spacer, write_number(decimal_number, "10"))


# convert base-10 number into chosen base
# assign suitable type to number (in this case, decimal)
if decimal_type == "decimal":
    # convert number type to a float (decimal)
    decimal_number = float(decimal_number)
    # split float into integer and fractional parts
    number_split_raw = split_decimals(decimal_number)
    # assign each part to a variable
    integer_part = number_split_raw[0]
    fractional_part = number_split_raw[1]

    # convert each part into the new base, separately
    new_integer_part = convert_integer(integer_part, new_base, alphabet)
    new_fractional_part = convert_fractional(fractional_part, new_base, alphabet)

    # concatenate the converted number and store convert number as a string
    converted_number = "{}.{}".format(str(new_integer_part), str(new_fractional_part))

# number type myst be an integer
else:
    # convert number type to an integer
    decimal_number = int(decimal_number)
    # convert number into the new base
    new_integer_part = convert_integer(decimal_number, new_base, alphabet)
    # store convert number as a string
    converted_number = "{}".format(str(new_integer_part))

# attach base in subscript to each version of number
original_number_print = write_number(decimal_number, "10")  # input base 10
converted_number_print = write_number(converted_number, new_base)

# align fourth line with previous lines using another space
spacer_two = " "*(len(number_label_base) - len(original_number_print))
# print number in both the old base and the new base
output_line_four = "{}{} = {}".format(spacer_two, original_number_print, converted_number_print)

# print text output
print("\nThe full expansion is:")
print()
print(output_line_one)
print(output_line_two)
print(output_line_three)
print()
print(output_line_four)
