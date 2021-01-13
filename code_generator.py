''' Path Function TBD '''

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

def _betel_transformation(alphabet, text, key, s=1):
    ''' '''
    return "".join(msg)

def _run():
    _text_filename = input("Enter filename: ")
    _modulus = input("Enter modulus number: ")
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
    path0 = _path_shift(alphabet_list, msg0)
    print("path0: ", path0)
    path1 = _path_shift(alphabet_list, msg1)
    print("path1: ", path1)
    path2 = _path_shift(alphabet_list, msg2)
    print("path2: ", path2)
    double_msg0 = _double_func_add(alphabet_list, msg0)
    print("double + ", double_msg0)
    double_msg1 = _double_func_sub(alphabet_list, msg1)
    print("double - ", double_msg1)

_run()
