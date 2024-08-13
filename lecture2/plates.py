def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    validity = length_requirement(s)
    if validity == False:
        return False
    else: 
        validity = alhpabet_requirement(s)
    if validity == False:
        return False
    else: 
        validity = digits_requirement(s)
    if validity == False:
        return False
    else: 
        validity = isvalid_requirement(s)
    if validity == False:
        return False
    else:
        return True

def length_requirement(s):
    if 2 <= len(s) <= 6:
        return True 
    else:
        return False

def alhpabet_requirement(s):
    if s[0].isalpha() == True and s[1].isalpha() == True:
        return True 
    else:
        return False

def digits_requirement(s):
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == '0':
                return False
            for j in range(i, len(s)):
                if not s[j].isdigit():
                    return False
            break
    return True


def isvalid_requirement(s):
    return s.isalnum()


main()