# by Uvajda (Karl Zander) - KryptoMagick 2021

''' Egyptian Star Code Generator version AAA '''

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
    msg = []
    if mask == 4:
        msg0 = []
        msg1 = []
        msg2 = []
        for x in range(textlen):
            number = ord(text[x]) - 65
            key_number = ord(key[x]) - 65
            output = (number + key_number) % 26
            letter = alphabet[output]
            msg0.append(letter)
        
        for x in range(textlen):
            number = ord(text[x]) - 65
            key_number = ord(key[x]) - 65
            output = (key_number - number) % 26
            letter = alphabet[output]
            msg1.append(letter)
        
        for x in range(textlen):
            number = ord(text[x]) - 65
            key_number = ord(key[x]) - 65
            output = (key_number + number) % 26
            letter = alphabet[output]
            msg2.append(letter)
    return msg0, msg1, msg2

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

def _hebew_transformation(alphabet, text, s=1):
    ''' Hebew Transformation '''
    double = _double_func_add(alphabet, text)
    RS = _right_shift_beta(alphabet, double)
    LS = _left_shift_beta(alphabet, RS)
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
    msg0, msg1, msg2 = _code_generator(record.text, alphabet, record.keys, m)
    print("phase0: m0", msg0, "phase0: m1", msg1, "phase0: m2", msg2)
    msg0, msg1, msg2 = _code_generator(msg0, alphabet, msg0, m)
    print("phase1: m0", msg0, "phase0: m1", msg1, "phase0: m2", msg2)
    msg0, msg1, msg2 = _code_generator(msg0, alphabet, msg0, m)
    print("phase2: m0", msg0, "phase0: m1", msg1, "phase0: m2", msg2)
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

_run()
