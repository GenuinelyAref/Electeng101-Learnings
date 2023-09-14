def current_divider(input_current, r_relevant, r_other):
    return input_current*((1/r_relevant)/((1/r_relevant)+(1/r_other)))


def voltage_divider(input_voltage, r_relevant, r_all):
    return input_voltage*(r_relevant/r_all)


r1 = 8200
rx = 6000
r2 = 2200
i_s = 0.010
v_s = 18

i1 = current_divider(i_s, r1+rx, r2)

# current source
current_v_x = rx*i1

# voltage source
voltage_v_x = voltage_divider(v_s, rx, rx + r1 + r2)

v0 = v_s - (voltage_v_x + current_v_x)

print("\n\nYAY FINAL ANSWER: {}\n\n".format(round(v0, 5)))
