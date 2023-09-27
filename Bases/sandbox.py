# program to expand out number in terms of its base

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
    var_return_num = "{}{}".format(var_num, special_num(var_base, "sub", "+"))
    return var_return_num


# expand a single digit using base and place-value
def expanded_term(var_digit, var_base, var_place_value, var_sign):
    var_expanded_term = "{}x{}{}".format(var_digit, var_base, special_num(var_place_value, "super", var_sign))
    return var_expanded_term


# fully expand the number
def full_expansion(var_num, var_base):
    # define output variable
    expanded_text = ""
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

    # if number has a decimal point
    else:
        # go down each digit
        for digit_index in range(0, var_digits):
            # get power of base
            var_placeholder = dot_index - digit_index - 1
            # adjust negative powers to display correctly
            if var_placeholder < 0:
                var_sign = "-"
                var_placeholder = var_placeholder * -1
            else:
                var_sign = "+"
            # get digit from number
            var_digit = str_var_num[digit_index]
            # if it's not the last digit, add a "+" and <space> at the end
            if digit_index != var_digits - 1:
                # expand the digit out using base and place-value
                expanded_text += "{} + ".format(expanded_term(var_digit, var_base, var_placeholder, var_sign))
            # otherwise no space or plus sign
            else:
                # expand the digit out using base and place-value
                expanded_text += "{}".format(expanded_term(var_digit, var_base, var_placeholder, var_sign))

    # return expanded form of number
    return expanded_text


number = 92.374
base = 10
w = write_number(number, base)
f = full_expansion(number, base)
print("{} = {}".format(w, f))