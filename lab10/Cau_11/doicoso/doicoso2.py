def loc(s):
    taphop="0123456789ABCDEF"
    s=s.upper()
    return ''.join(c for c in s if c in taphop)
def hecoso(s):
    s=s.upper()
    if all(c in '01' for c in s):
        return 2
    elif all(c in '0123456789' for c in s):
        return 10
    elif all(c in '0123456789ABCDEF' for c in s):
        return 16
    else:
        return -1
def he_2_sang_10(s):
    return int(s,2)
def he_8_sang_10(s):
    return int(s,8)
def he_16_sang_10(s):
    return int(s,16)

