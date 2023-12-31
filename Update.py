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


def decryptor(n, m, r, cipher, Accname, key_pair):
    t = [m[i] + n[i] for i in range(len(m))]
    print("t---->",t)
    t.append(m[len(m) - 1] + n[len(n) - 1])
    q = t[0] ^ t[1]
    print("q----->",q)
    for i in range(len(m) - 2):
        q = q ^ t[2 + i]

    return q

def updation(name, value, temp, temp1):
    with shelve.open('Ci', writeback=True) as db:
        r = db['random']
        cipher = db['cipher']
        Accname = db['Accname']
        key_pair = db['key_pair']
    print("Random-->",r)
    print("Cipher--->",cipher)
    print("ALL KEY-PAIRS-->",key_pair)
    print("KEY VALUE PAIR BEFORE UPDATION:")
    pos = Accname[name]
    pos = int(pos) + int(value)  # Convert to integers before addition
    y = temp
    x = temp1

    print("Old key:", key_pair[str(pos)])
    mask = cipher[pos]

    temp_keys = list(key_pair[str(pos)].keys())
    temp_values = list(key_pair[str(pos)].values())

    temp = [r[int(temp_keys[i])] for i in range(3)]
    temp1 = [cipher[int(temp_values[i])] for i in range(3)]
    print(temp,temp1)

    n = decryptor(temp, temp1, r, cipher, Accname, key_pair)
    print("crt value-->",n)
    encryptop(x, y, n, pos, r, cipher, Accname, key_pair)

    print("Updated cipher:", cipher[pos])

    for i in range(pos + 1, len(cipher)):
        keys_i = list(key_pair[str(i)].keys())
        values_i = list(key_pair[str(i)].values())
        keys_i=[int(x) for x in keys_i]
        values_i=[int(x) for x in values_i]
        if pos in values_i:
            temp1 = [mask if int(values_i[i]) == pos else cipher[int(values_i[i])] for i in range(3)]
            temp = [r[int(keys_i[i])] for i in range(3)]

            ans = decryptor(temp, temp1, r, cipher, Accname, key_pair)
            print(ans)
            encryptop(x, y, ans, i, r, cipher, Accname, key_pair)

    with shelve.open('Ci', writeback=True) as db:
        db['cipher'] = cipher
        db['Accname'] = Accname
        db['key_pair'] = key_pair
    print("Random-->",r)
    print("cipher--->",cipher)
    print("UPDATED ALL KEY_PAIRS-->",key_pair)
    print("KEY VALUE PAIR AFTER UPDATION:")
    print(key_pair[str(pos)])

