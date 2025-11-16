import string

def pass_validator():
    p = input("Enter your desired password:  ")
    if has_min_length(p) and has_uppercase(p) and has_lowercase(p) and has_digit(p) and has_special_char(p):
        print("the entered password is valid")
        return
    print("the entered password is NOT valid!")
    pass_validator()

def has_min_length(p):
    return len(p) >= 12

def has_uppercase(p):
    for char in p:
        if char.isupper():
            return True
    return False
def has_lowercase(p):
    for char in p:
        if char.islower():
            return True
    return False
def has_digit(p):
    for char in p:
        if char.isdigit():
            return True
    return False
def has_special_char(p):
    for char in p:
        if char in string.punctuation:
            return True
    return False

pass_validator()