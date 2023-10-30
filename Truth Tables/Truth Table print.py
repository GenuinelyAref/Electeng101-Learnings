# this program is used in experimenting the creation of truth tables and if any generalisation can be made about
# any boolean expression comprising x unique inputs


# convert integer part into new base
def convert_integer(var_int_part, var_new_base, var_alphabet):
    # define used variables
    var_converted_num = ""
    var_alphabet_indices = []
    if var_int_part == 0:
        return 0
    else:
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


def adjust_spacing(var_num, var_max_length):
    var_num = str(var_num)
    while len(str(var_num)) != var_max_length:
        var_num = "0" + var_num
    return var_num


binary_list = []
num_terms = 1
max_length = len(convert_integer(2 ** num_terms - 1, 2, ["0", "1"]))
for unique_input in range(0, 2 ** num_terms):
    binary_num = convert_integer(unique_input, 2, ["0", "1"])
    binary_num = adjust_spacing(binary_num, max_length)
    binary_list.append(binary_num)
    print(binary_num)

for row in range(0, 2 ** num_terms):
    for col in range(0,)