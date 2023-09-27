# program to expand out number in terms of its base

# function to retrieve subscript character unicode equivalent for any digit (0-9)
def special_num(num, var_type):
    # define subscript unicode character lists
    if var_type == "sub":
        unicode_chars = ['\u2080', '\u2081', '\u2082', '\u2083', '\u2084',
                         '\u2085', '\u2086', '\u2087', '\u2088', '\u2089']
    # define superscript unicode character list
    else:
        unicode_chars = ['\u2070', '\u00b9', '\u00b2', '\u00b3', '\u2074',
                         '\u2075', '\u2076', '\u2077', '\u2078', '\u2079']
    # define used variable
    subscript_text = ""
    # repeat for each digit in the number provided
    for i in range(0, len(str(num))):
        # convert each digit into its subscript unicode equivalent
        subscript_text += unicode_chars[int((str(num))[i])]
    # return subscript unicode equivalent to caller (ready to print)
    return subscript_text


def expanded_term(var_digit, var_base, var_place_value):
    expanded_term = "{}x{}{}".format(var_digit, var_base, special_num(var_place_value, "super"))
    return expanded_term


def full_expansion(var_num, var_base):
    expanded_text = ""
    str_var_num = list(str(var_num))
    try:
        dot_index = str_var_num.index(".")
        str_var_num.pop(dot_index)
    except ValueError:
        dot_index = -1
        pass
    var_digits = len(str_var_num)
    if dot_index == -1:
        for digit in range(var_digits-1, -1, -1):
            var_digit = str_var_num[var_digits - digit - 1]
            if digit != 0:
                expanded_text += "{} + ".format(expanded_term(var_digit, var_base, digit))
            else:
                expanded_text += "{}".format(expanded_term(var_digit, var_base, digit))
    else:
        for digit in range(var_digits, -1, -1):
            if digit > dot_index:
                var_placeholder = digit - dot_index - 1
                var_digit = str_var_num[var_placeholder]
                expanded_text += "{} + ".format(expanded_term(var_digit, var_base, var_placeholder))
            elif digit < dot_index:
                var_placeholder = digit - dot_index
                var_digit = str_var_num[var_placeholder]
                expanded_text += "{} + ".format(expanded_term(var_digit, var_base, var_placeholder))
    return expanded_text


f = full_expansion(321, 10)
print(f)