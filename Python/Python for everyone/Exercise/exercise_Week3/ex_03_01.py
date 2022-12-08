hrs = input("Enter Hours:")
h = float(hrs)
hrate = input("Enter Rate per hour")
hr = float(hrate)
if h <= 40 :
    print(hr * h)
else :
    print(40 * hr + (h - 40) * hr * 1.5)
