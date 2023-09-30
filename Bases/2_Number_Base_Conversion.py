# program to convert a number from decimal base to a different base
import math


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
    # add subscript value to number
    var_return_num = "{}{}".format(var_num, special_num(var_base, "sub", "+"))
    # return text value
    return var_return_num


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


# get base value from user
def get_base():
    base_valid = False
    # repeat until base input is valid
    while not base_valid:
        # get input from user
        var_base = input("\nWhat base do you want to change the number into? Enter a number (>1) here: ")
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


# convert integer part into new base
def convert_integer(var_int_part, var_new_base):
    var_converted_num = ""
    while var_int_part != 0:
        # calculate digits starting from least significant digit
        var_remainder = var_int_part % var_new_base
        var_int_part = var_int_part // var_new_base
        var_converted_num = "{}{}".format(var_remainder, var_converted_num)
    return int(var_converted_num)


# convert fractional part into new base
def convert_fractional(var_fractional_part, var_new_base):
    var_fractional_part = float("0.{}".format(str(var_fractional_part)))
    # var_fractional_part = 0.625
    var_converted_num = ""
    while var_fractional_part != 0:
        # calculate digits starting from least significant digit
        var_int_part = math.floor(var_fractional_part * var_new_base)
        # var_int_part = 1
        var_fractional_part = (var_fractional_part * var_new_base) - var_int_part
        var_converted_num = "{}{}".format(var_converted_num, var_int_part)
    return int(var_converted_num)


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
print("Number base conversion\n\n")

# get type of input (decimal or integer number)
num_type = get_type()

# get number
number = input("\nEnter your number: ")

# get base value
new_base = get_base()

# assign suitable type to number
if num_type == "decimal":
    # convert number type to a float (decimal)
    number = float(number)
    # split float into integer and fractional parts
    number_split_raw = split_decimals(number)
    # assign each part to a variable
    integer_part = number_split_raw[0]
    fractional_part = number_split_raw[1]

    # convert each part into the new base, separately
    new_integer_part = convert_integer(integer_part, new_base)
    new_fractional_part = convert_fractional(fractional_part, new_base)

    # concatenate the converted number and store convert number as a string
    converted_number = "{}.{}".format(str(new_integer_part), str(new_fractional_part))

else:
    # convert number type to an integer
    number = int(number)
    # convert number into the new base
    new_integer_part = convert_integer(number, new_base)
    # store convert number as a string
    converted_number = "{}".format(str(new_integer_part))

# attach base in subscript to each version of number
original_number_print = write_number(number, "10")  # input base 10
converted_number_print = write_number(converted_number, new_base)
# add newline
print()
# print number in both the old base and the new base
print("{} = {}".format(original_number_print, converted_number_print))
