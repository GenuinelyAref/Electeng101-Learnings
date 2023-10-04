# Dividers (current & voltage)

# current divider function
def current_divider(input_current, r_relevant, r_other):
    return input_current*((1/r_relevant)/((1/r_relevant)+(1/r_other)))


# voltage divider function
def voltage_divider(input_voltage, r_relevant, r_all):
    return input_voltage*(r_relevant/r_all)

