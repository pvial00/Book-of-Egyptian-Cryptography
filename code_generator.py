# by Uvajda (Karl Zander) - KryptoMagick 2021

''' Egyptian Star Code Generator version AAB '''

class Record:
    text ={}
    keys = {}
    modulus = 0
    mask = 0
    result = {}
    path = {}

def _file_reader(filename, record):
    fd = open(filename, "r")
    data = fd.read()
    fd.close()
    textline = data.split('\n')[0]
    keyline = data.split('\n')[1]
    text = textline.split()
    key = keyline.split()
    textline_len = len(textline)
    
    for c in range(textline_len):
        record.text[c] = textline[c]
        record.keys[c] = keyline[c]
    return record

def _alphabet_generator(n):
    alphabet = {}
    alphabet_list = []
    for c in range(n):
        x = c % 26
        letter = chr(x  + 65)
        alphabet[x % 26] = letter
        alphabet_list.append(letter)
    return alphabet, alphabet_list

def _code_generator(text, alphabet, key, mask):
    textlen = len(text)
    modulus = textlen
    msg = []
    if mask == 4:
        msg0 = []
        msg1 = []
        msg2 = []
        m = []
        msg0_m = []
        msg1_m = []
        msg2_m = []
        msg0_p = []
        msg1_p = []
        msg2_p = []

        for x in range(textlen):
            number = ord(text[x]) - 65
            key_number = ord(key[x]) - 65
            output = (number + key_number) % 26
            letter = alphabet[output]
            msg0.append(letter)
        L0 = _line_converter("".join(msg0))
        L0_m = _line_multiplier(L0, L0, modulus)
        L0_p = _line_power(L0, L0, modulus)
        
        for x in range(textlen):
            number = ord(text[x]) - 65
            key_number = ord(key[x]) - 65
            output = (key_number - number) % 26
            letter = alphabet[output]
            msg1.append(letter)
        L1 = _line_converter("".join(msg1))
        L1_m = _line_multiplier(L1, L1, modulus)
        L1_p = _line_power(L1, L1, modulus)
        
        for x in range(textlen):
            number = ord(text[x]) - 65
            key_number = ord(key[x]) - 65
            output = (key_number + number) % 26
            letter = alphabet[output]
            msg2.append(letter)
        L2 = _line_converter("".join(msg2))
        L2_m = _line_multiplier(L2, L2, modulus)
        L2_p = _line_power(L2, L2, modulus)
    return msg0, msg1, msg2, L0, L0_m, L0_p, L1, L1_m, L1_p, L2, L2_m, L2_p, modulus

def _double_func_add(alphabet, text):
    textlen = len(text)
    msg = []
    for x in range(textlen):
        number = ord(text[x]) - 65
        output = (number + number) % 26
        letter = alphabet[output]
        msg.append(letter)
    return "".join(msg)

def _double_func_sub(alphabet, text):
    textlen = len(text)
    msg = []
    for x in range(textlen):
        number = ord(text[x]) - 65
        for y in range(number):
            alphabet.append(alphabet.pop(0))
        letter = alphabet[number]
        msg.append(letter)
    return "".join(msg)

def _double_func_sub_sub(alphabet, text):
    textlen = len(text)
    msg = []
    for x in range(textlen):
        number = ord(text[x]) - 65
        output = (number - number) % 26
        letter = alphabet[output]
        msg.append(letter)
    return "".join(msg)

def _path_shift(alphabet, text, s=1):
    textlen = len(text)
    msg = []
    for x in range(textlen):
        number = ord(text[x]) - 65
        for y in range(s):
            alphabet.append(alphabet.pop(0))
        letter = alphabet[number]
        msg.append(letter)
    return "".join(msg)

def _left_shift_beta(alphabet, text, s=1):
    textlen = len(text)
    msg = []
    for x in range(textlen):
        number = ord(text[x]) - 65
        for y in range(s):
            alphabet.insert(0, alphabet.pop(25))
        letter = alphabet[number]
        msg.append(letter)
    return "".join(msg)

def _right_shift_beta(alphabet, text, s=1):
    textlen = len(text)
    msg = []
    for x in range(textlen):
        number = ord(text[x]) - 65
        for y in range(s):
            alphabet.insert(0, alphabet.pop(25))
        letter = alphabet[number]
        msg.append(letter)
    return "".join(msg)

def _right_shift_alpha(alphabet, text, s):
    result = []
    textlen = len(text)
    for x in range(textlen):
        number = ord(text[x]) - 65
        output = (number + s) % 26
        letter = alphabet[output]
        result.append(letter)
    return "".join(result)

def _left_shift_alpha(alphabet, text, s):
    result = []
    textlen = len(text)
    for x in range(textlen):
        number = ord(text[x]) - 65
        output = (number - s) % 26
        letter = alphabet[output]
        result.append(letter)
    return "".join(result)

def _betel_shift_alpha(alphabet, keyword):
    result = []
    textlen = len(keyword)
    shift_order = [1, 9, 0, 9, 0]
    for x in range(5):
        number = ord(keyword[x]) - 65
        output = (number + shift_order[x]) % 26
        letter = alphabet[output]
        result.append(letter)
    return "".join(result)

def _betel_shift_beta(alphabet, keyword):
    result = []
    textlen = len(keyword)
    shift_order = [0, 0, 9, 0, 0]
    for x in range(5):
        number = ord(keyword[x]) - 65
        output = (number - shift_order[x]) % 26
        letter = alphabet[output]
        result.append(letter)
    return "".join(result)

def _betel_shift_gamma(alphabet, keyword):
    result = []
    textlen = len(keyword)
    shift_order = [2, 10, 2, 10, 1]
    for x in range(5):
        number = ord(keyword[x]) - 65
        output = (number - shift_order[x]) % 26
        letter = alphabet[output]
        result.append(letter)
    return "".join(result)

def _betel_shift_omega(alphabet, keyword):
    result = []
    textlen = len(keyword)
    shift_order = [0, 10, 0, 10, 0]
    for x in range(5):
        number = ord(keyword[x]) - 65
        output = (number - shift_order[x]) % 26
        letter = alphabet[output]
        result.append(letter)
    return "".join(result)

def _line_converter(line, prefix=None):
    n = []
    if prefix != None:
        n.append(prefix)
    for char in line:
        n.append(str(ord(char) - 65))
    return int("".join(n))

def _line_multiplier(a, b, m):
    return ((a * b) % m)

def _line_power(a, b, m):
    return pow(a, b, m)

def _line_square(a):
    return (a ** a)

def _line_square_mod(a, m):
    return ((a ** a) % m)

def _line_xor(a, m):
    return ((a ^ a))

def _line_add(a, m):
    return ((a + a) & 0xFFFFFFFFFFFFFFFF)

def _line_subtract(a, m):
    return ((a - a) & 0xFFFFFFFFFFFFFFFF)

def _number_to_string(n):
    return str(n)

def _hebew_transformation(alphabet, text, s=1):
    ''' Hebew Transformation '''
    double = _double_func_add(alphabet, text)
    RS = _right_shift_beta(alphabet, double)
    LS = _right_shift_beta(alphabet, RS)
    return double, "".join(RS), "".join(LS)

def _wind_transformation(alphabet, text, s=2):
    ''' Wind Transformation '''
    ''' Untested '''
    double = _double_func_add(alphabet, text)
    RS = _right_shift_beta(alphabet, double)
    LS = _left_shift_beta(alphabet, RS)
    return double, "".join(RS), "".join(LS)

def _radio_transformation(alphabet, text, s=2):
    ''' Venus Radio Transformation '''
    ''' Untested '''
    double = _double_func_add(alphabet, text)
    RS = _right_shift_alpha(alphabet, double, 5)
    LS = _left_shift_alpha(alphabet, RS, 2)
    return double, "".join(RS), "".join(LS)

def _asia_transformation(alphabet, text, s=2):
    ''' Asia Transformation '''
    ''' Untested '''
    double = _double_func_add(alphabet, text)
    RS = _right_shift_alpha(alphabet, double, 5)
    LS = _left_shift_alpha(alphabet, RS, 2)
    return double, "".join(RS), "".join(LS)

def _au_transformation(alphabet, text, s=2):
    ''' Au Transformation '''
    ''' Untested '''
    double = _double_func_add(alphabet, text)
    RS = _right_shift_alpha(alphabet, double, 5)
    LS = _left_shift_alpha(alphabet, RS, 2)
    return double, "".join(RS), "".join(LS)

def _betel_transformation(alphabet, text, s=2):
    ''' Betel Transformation '''
    double = _double_func_add(alphabet, text)
    RS = _right_shift_alpha(alphabet, double, 5)
    LS = _left_shift_alpha(alphabet, RS, 2)
    return double, "".join(RS), "".join(LS)

def _artrax_transformation(alphabet, text, s=2):
    ''' Artax Transformation '''
    ''' Untested '''
    double = _double_func_add(alphabet, text)
    RS = _right_shift_alpha(alphabet, double, 3)
    LS = _left_shift_alpha(alphabet, RS, 2)
    return double, "".join(RS), "".join(LS)

def _wajdet_transformation(alphabet, text, s=2):
    ''' Wajdet Transformation '''
    ''' Untested '''
    double = _double_func_add(alphabet, text)
    triple = _double_func_add(alphabet, double)
    LS = _left_shift_alpha(alphabet, triple, 5)
    RS = _right_shift_alpha(alphabet, LS, 2)
    return double, "".join(RS), "".join(LS)

def _psy_transformation(alphabet, text, s=2):
    ''' Psy Transformation '''
    ''' Untested '''
    double = _double_func_sub_sub(alphabet, text)
    triple = _double_func_sub_sub(alphabet, double)
    RS = _right_shift_alpha(alphabet, triple, 5)
    LS = _left_shift_alpha(alphabet, RS, 2)
    return double, triple, "".join(RS), "".join(LS)

def _betel_heqet_venus_transformation(alphabet, text, s=2):
    ''' Betel Heqet Venus Transformation '''
    double = _double_func_add(alphabet, text)
    triple = _double_func_add(alphabet, double)
    bsA = _betel_shift_alpha(alphabet, double)
    bsB = _betel_shift_beta(alphabet, bsA)
    bsG = _betel_shift_gamma(alphabet, bsB)
    return double, triple, bsB, bsG

def _U_transformation(alphabet, text, s=2):
    ''' U Transformation '''
    double = _double_func_add(alphabet, text)
    triple = _double_func_add(alphabet, double)
    bsA = _betel_shift_alpha(alphabet, double)
    bsB = _betel_shift_beta(alphabet, bsA)
    return double, triple, bsB, bsA

def _run():
    _text_filename = input("Enter filename: ")
    _modulus = input("Enter modulus number: ")
    _keyword = input("Enter keyword: ")
    n = int(_modulus)
    m = 4
    
    record = Record()
    record.modulus = n
    record.mask = m
    
    record = _file_reader(_text_filename, record)
    alphabet, alphabet_list = _alphabet_generator(n)
    msg0, msg1, msg2, L0, L0_m, L0_p, L1, L1_m, L1_p, L2, L2_m, L2_p, modulus = _code_generator(record.text, alphabet, record.keys, m)
    print("phase0: m0", msg0, "phase0: m1", msg1, "phase0: m2", msg2)

    print("Line0 as an integer ", L0)
    print("Line1 as an integer ", L1)
    print("Line2 as an integer ", L2)

    print("Line0 multiplied ", L0_m)
    print("Line1 multiplied ", L1_m)
    print("Line2 multiplied ", L2_m)
    
    print("Line0 raised to iteself ", L0_p, " modulo line modulus", modulus)
    print("Line1 raised to iteself ", L1_p, " modulo line modulus", modulus)
    print("Line2 raised to iteself ", L2_p, " modulo line modulus", modulus)
    
    msg0, msg1, msg2, L0, L0_m, L0_p, L1, L1_m, L1_p, L2, L2_m, L2_p, modulus = _code_generator(msg0, alphabet, msg0, m)
    print("phase1: m0", msg0, "phase0: m1", msg1, "phase0: m2", msg2)

    print("Line0 as an integer ", L0)
    print("Line1 as an integer ", L1)
    print("Line2 as an integer ", L2)

    print("Line0 multiplied ", L0_m)
    print("Line1 multiplied ", L1_m)
    print("Line2 multiplied ", L2_m)
    
    print("Line0 raised to iteself ", L0_p, " modulo line modulus", modulus)
    print("Line1 raised to iteself ", L1_p, " modulo line modulus", modulus)
    print("Line2 raised to iteself ", L2_p, " modulo line modulus", modulus)

    msg0, msg1, msg2, L0, L0_m, L0_p, L1, L1_m, L1_p, L2, L2_m, L2_p, modulus  = _code_generator(msg0, alphabet, msg0, m)
    
    print("Line0 as an integer ", L0)
    print("Line1 as an integer ", L1)
    print("Line2 as an integer ", L2)

    print("Line0 multiplied ", L0_m)
    print("Line1 multiplied ", L1_m)
    print("Line2 multiplied ", L2_m)
    
    print("Line0 raised to the power of the line modulus", L0_p)
    print("Line1 raised to the power of the line modulus", L1_p)
    print("Line2 raised to the power of the line modulus", L2_p)

    print("phase2: m0", msg0, "phase0: m1", msg1, "phase0: m2", msg2)
    
    print("Line0 as an integer ", L0)
    print("Line1 as an integer ", L1)
    print("Line2 as an integer ", L2)

    print("Line0 multiplied ", L0_m)
    print("Line1 multiplied ", L1_m)
    print("Line2 multiplied ", L2_m)
    
    print("Line0 raised to itself ", L0_p, " modulo line modulus", modulus)
    print("Line1 raised to itself ", L1_p, " modulo line modulus", modulus)
    print("Line2 raised to itself ", L2_p, " modulo line modulus", modulus)
    
    print("Line modulus", modulus)

    path0 = _path_shift(list(alphabet_list), msg0)
    print("path0: ", path0)
    path1 = _path_shift(list(alphabet_list), msg1)
    print("path1: ", path1)
    path2 = _path_shift(list(alphabet_list), msg2)
    print("path2: ", path2)
    double_msg0 = _double_func_add(list(alphabet_list), msg0)
    print("double + ", double_msg0)
    double_msg1 = _double_func_sub(list(alphabet_list), msg1)
    print("double - ", double_msg1)
    hebewD, hebewB, hebewA = _hebew_transformation(list(alphabet_list), msg0)
    print("Hebew Delta", hebewD)
    print("Hebew Transformations", hebewB, hebewA)
    betelD, betelB, betelA = _betel_transformation(list(alphabet_list), msg0)
    print("Betel Delta", betelD)
    print("Betel Transformations", betelB, betelA)
    betelHeqetVenusD, betelHeqetVenusT, betelHeqetVenusB, betelHeqetVenusA = _betel_heqet_venus_transformation(list(alphabet_list), _keyword)
    print("Betel Heqet Venus Delta", betelHeqetVenusD)
    print("Betel Heqet Venus T", betelHeqetVenusT)
    print("Betel Heqet Venus Transformations", betelHeqetVenusB, betelHeqetVenusA)
    print("Line0 as an integer ", L0)
    print("Line1 as an integer ", L1)
    print("Line2 as an integer ", L2)

    print("Line0 multiplied ", L0_m)
    print("Line1 multiplied ", L1_m)
    print("Line2 multiplied ", L2_m)
    
    print("Line0 raised to itself ", L0_p, " modulo line modulus", modulus)
    print("Line1 raised to itself ", L1_p, " modulo line modulus", modulus)
    print("Line2 raised to itself ", L2_p, " modulo line modulus", modulus)

    print("Line modulus", modulus)

_run()
