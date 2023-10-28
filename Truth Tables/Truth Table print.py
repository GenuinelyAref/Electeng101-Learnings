# this program is used in experimenting the creation of truth tables and if any generalisation can be made about
# any boolean expression comprising of x unique inputs


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

num_terms = 2
for unique_input in range(1, 2 ** num_terms + 1):
    print(unique_input)
