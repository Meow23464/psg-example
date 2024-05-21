def xnor(a, b):
    return (a and b) or (not a and not b)

print("XNOR Truth Table")
print(f"0 XNOR 0: {xnor(0, 0)}")
print(f"0 XNOR 1: {xnor(0, 1)}")
print(f"1 XNOR 0: {xnor(1, 0)}")
print(f"1 XNOR 1: {xnor(1, 1)}")
