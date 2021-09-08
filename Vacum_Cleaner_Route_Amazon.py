def Helper(st):
    dit = {}
    dit['L'] = 0
    dit['R'] = 0
    dit['U'] = 0
    dit['D'] = 0
    for i in st:
        try:
            dit[i] += 1
        except:
            dit[i] = 1


    if dit['L'] != dit['R']:
        return False
    elif dit['U'] != dit['D']:
        return False
    else:
        print("Reached initial position")
        return True

print(Helper("URURD"))


