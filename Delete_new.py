import random
import shelve

def decryptor(n, m, r, cipher, Accname, key_pair):
    t = [m[i] + n[i] for i in range(len(m)-1)]
    t.append(m[(len(m) - 1)] + n[(len(m) - 1)])
    q = (t[0] ^ t[1])

    for i in range(len(m) - 2):
        q = (q ^ t[2 + i])
    return q

def deletion(loc, r, cipher, Accname, key_pair):
    changes = dict()

    del key_pair[str(loc)]
    mask = cipher.pop(loc)

    for i in range(loc + 1, len(cipher)):
        var = key_pair[str(i)]
        temp = list(var.keys())

        if loc in var.values():
            temp1 = list(var.values())
            temp1 = [cipher[int(x)] if int(x) < loc else (mask if int(x) == loc else cipher[int(x) - 1]) for x in temp1]
            temp2 = [r[int(x)] for x in temp]
            lol = decryptor(temp2, temp1, r, cipher, Accname, key_pair)
            changes.update({str(i - 1): lol})

        for j in temp:
            if var[j] > loc:
                var[j] -= 1

    for i in range(loc + 1, len(cipher)):
        key_pair[str(i - 1)] = key_pair.pop(str(i))

    for key, value in changes.items():
        calculation(value, int(key), r, cipher, Accname, key_pair)

    return 0

def encryptop(x, y, n, pos, r, cipher, Accname, key_pair):
    dictionary = {str(y[i]): x[i] for i in range(2)}
    a, b = [], []

    for i in dictionary.keys():
        a.append(r[int(i)])

    for i in dictionary.values():
        b.append(cipher[i])

    a.append(r[y[2]])
    t = [b[i] + a[i] for i in range(2)]
    s = (t[0] ^ t[1])
    new_cipher = (n ^ s)
    new_cipher = round(new_cipher - a[2])

    dictionary.update({str(y[2]): pos})

    if pos < len(cipher):
        cipher[pos] = new_cipher
    else:
        cipher.append(new_cipher)

    key_pair.update({str(pos): dictionary})

def calculation(n, pos, r, cipher, Accname, key_pair):
    x = random.sample(range(0, pos - 1), 2)
    y = random.sample(range(0, len(r) - 1), 3)
    encryptop(x, y, n, pos, r, cipher, Accname, key_pair)

def deletion2(name):
    with shelve.open('Ci', writeback=True) as db:
        r = db['random']
        cipher = db['cipher']
        Accname = db['Accname']
        key_pair = db['key_pair']

    loc = Accname[name]

    for key, value in Accname.items():
        if value > loc:
            Accname[key] = value - 6

    for pos in range(loc, loc + 6):
        deletion(loc, r, cipher, Accname, key_pair)

    del Accname[name]

    with shelve.open('Ci', writeback=True) as db:
        db['cipher'] = cipher
        db['Accname'] = Accname
        db['key_pair'] = key_pair

    print("AFTER DELETION:")
    print("Accname-->",Accname)
    print("cipher-->",cipher)
    print("Key_Pair-->",key_pair)

