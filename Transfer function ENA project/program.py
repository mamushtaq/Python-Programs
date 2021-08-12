import math
f = 1
while f != "end":
    f = input("Enter value of f = ")
    af = 12
    fl = 500
    fh = 10000
    div = float(f)/float(fl)
    numerator = float(af) * div
    den1 = math.sqrt(1 + (float(f)/float(fl))**2)
    den2 = math.sqrt(1 + (float(f)/float(fh))**2)
    Hs = float(numerator)/(float(den1)*float(den2))
    print(f"The value of gain at frequency {f} = {Hs}")