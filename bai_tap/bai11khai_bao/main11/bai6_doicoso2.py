# doicoso2.py

def is_binary_string(s):
    return all(c in '01' for c in s)

def binary_to_dec(s):
    return int(s, 2)

def oct_to_dec(s):
    return int(s, 8)

def hex_to_dec(s):
    return int(s, 16)
