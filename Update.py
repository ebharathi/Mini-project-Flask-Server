import random
import shelve

def encryptop(x, y, n, pos, r, cipher, Accname, key_pair):
    key_dict = {str(y[i]): x[i] for i in range(2)}
    a, b = [], []

    for i in key_dict.keys():
        a.append(r[int(i)])

    for i in key_dict.values():
        b.append(cipher[i])

    a.append(r[y[2]])
    t = [b[i] + a[i] for i in range(2)]
    s = (t[0] ^ t[1])
    new_cipher = (n ^ s)
    new_cipher = round(new_cipher - a[2])

    key_dict.update({str(y[2]): pos})

    if pos < len(cipher):
        cipher[pos] = new_cipher
    else:
        cipher.append(new_cipher)

    key_pair.update({str(pos): key_dict})

def calculation(n, pos, r, cipher, Accname, key_pair):
    x = random.sample(range(0, pos - 1), 2)
    y = random.sample(range(0, len(r) - 1), 3)
    encryptop(x, y, n, pos, r, cipher, Accname, key_pair)
    print("Updated Cipher:", cipher, "\nSuccessfully inserted")

def decryptor(n, m, r, cipher, Accname, key_pair):
    t = [m[i] + n[i] for i in range(len(m) - 1)]
    t.append(m[(len(m) - 1)] + n[(len(m) - 1)])
    q = (t[0] ^ t[1])

    for i in range(len(m) - 2):
        q = (q ^ t[2 + i])

    return q

def updation(name, value, temp, temp1):
    with shelve.open('Ci', writeback=True) as db:
        r = db['random']
        cipher = db['cipher']
        Accname = db['Accname']
        key_pair = db['key_pair']

    print("KEY VALUE PAIR BEFORE UPDATION:")
    pos = Accname[name]
    pos += value
    y = temp
    x = temp1

    print("Old key:", key_pair[str(pos)])
    mask = cipher[pos]

    temp_keys = list(key_pair[str(pos)].keys())
    temp_values = list(key_pair[str(pos)].values())

    temp = [r[int(temp_keys[i])] for i in range(2)]
    temp1 = [cipher[int(temp_values[i])] for i in range(2)]

    n = decryptor(temp, temp1, r, cipher, Accname, key_pair)
    encryptop(x, y, n, pos, r, cipher, Accname, key_pair)

    print("Updated cipher:", cipher[pos])

    for i in range(pos + 1, len(cipher)):
        keys_i = list(key_pair[str(i)].keys())
        values_i = list(key_pair[str(i)].values())

        if pos in values_i:
            temp1 = [mask if int(values_i[i]) == pos else cipher[int(values_i[i])] for i in range(2)]
            temp = [r[int(keys_i[i])] for i in range(2)]

            ans = decryptor(temp, temp1, r, cipher, Accname, key_pair)
            encryptop(x, y, ans, i, r, cipher, Accname, key_pair)

    with shelve.open('Ci', writeback=True) as db:
        db['cipher'] = cipher
        db['Accname'] = Accname
        db['key_pair'] = key_pair

    print("KEY VALUE PAIR AFTER UPDATION:")
    print(key_pair[str(pos)])

