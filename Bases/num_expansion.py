# program to expand out number in terms of its base

# function to retrieve subscript character unicode equivalent for any digit (0-9)
def special_num(num, var_type, sign):
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
    for i in range(0, len(str(num))):
        # convert each digit into its subscript unicode equivalent
        special_text += unicode_chars[int((str(num))[i])]
    if sign == "-":
        special_text = negative_superscript + special_text
    # return subscript unicode equivalent to caller (ready to print)
    return special_text


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
        for digit in range(var_digits - 1, -1, -1):
            # get digit from number
            var_digit = str_var_num[var_digits - digit - 1]
            # if it's not the last digit, add a "+" and <space> at the end
            if digit != 0:
                expanded_text += "{} + ".format(expanded_term(var_digit, var_base, digit, "+"))
            # otherwise no space or plus sign
            else:
                expanded_text += "{}".format(expanded_term(var_digit, var_base, digit, "+"))
    
    # if number has a decimal point
    else:
        # go down each digit
        for digit in range(0, var_digits):
            # get power of base
            var_placeholder = dot_index - digit - 1
            # adjust negative powers to display correctly
            if var_placeholder < 0:
                var_sign = "-"
                var_placeholder = var_placeholder * -1
            else:
                var_sign = "+"
            # get digit from list
            var_digit = str_var_num[digit]
            # if it's not the last digit, add a "+" and <space> at the end
            if digit != var_digits - 1:
                expanded_text += "{} + ".format(expanded_term(var_digit, var_base, var_placeholder, var_sign))
            # otherwise no space or plus sign
            else:
                expanded_text += "{}".format(expanded_term(var_digit, var_base, var_placeholder, var_sign))

    return expanded_text


f = full_expansion(9365.4128376, 10)
print(f)