def calculator(fnumber , op , snumber):
    try:
        if op == '+':
            print(f"{fnumber} {op} {snumber} = {fnumber+snumber}")
        elif op == '-':
            print(f"{fnumber} {op} {snumber} = {fnumber-snumber}")
        elif op == '*':
            print(f"{fnumber} {op} {snumber} = {fnumber*snumber}")
        elif op == '/':
            print(f"{fnumber} {op} {snumber} = {fnumber/snumber}")
    except ZeroDivisionError:
        print("****CAN'T DIVIDE BY ZERO****")