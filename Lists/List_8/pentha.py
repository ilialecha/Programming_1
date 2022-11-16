from easyinput import read_line


def is_pentha(s):
    return "a" in s and "e" in s and "i" in s and "o" in s and "u" in s


def are_pentha(ss):
    for s in ss.split():
        if not is_pentha(s): return False
    return True

print(are_pentha("                   "))

ss = read_line()

p = False

while ss is not None and ss.strip()!="" and not p:
    if are_pentha(ss) and ss!= "" : print(ss) ; p = not p
    ss = read_line()
if not p: print("No all-pentavocalic line was found")


