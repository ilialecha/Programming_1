from easyinput import read_line

data = read_line()
found = False
while data is not None:
    total = 0
    #Processing data
    if data.split()[-1] == "cash":
        for item in sorted(data.split()[:-1], key=lambda x: float(x), reverse=True):
            total += float(item)
            if total > 1000.00:
                print("Somebody paid over 1000 euros in cash!")
                found = not found
                break
    if found : break
    #Obtaining new input
    data = read_line()

if not found: print("Nobody paid over 1000 euros in cash.")