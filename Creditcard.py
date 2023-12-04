import random
import shelve

def decryptor(n, m, r, cipher, Accname, key_pair):
    t = [m[i] + n[i] for i in range(len(m) - 1)]
    t.append(m[len(m) - 1] + n[len(n) - 1])
    q = t[0] ^ t[1]

    for i in range(len(m) - 2):
        q = q ^ t[2 + i]

    return q

def decryption2(name, message):
    try:
        with shelve.open('Ci') as db:
            r = db['random']
            cipher = db['cipher']
            Accname = db['Accname']
            key_pair = db['key_pair']

        print("Accname:", Accname)
        print("Name:", name)
        print("Message:", message)

        loc = Accname[name]
        print("Location:", loc)

        for de in range(0, 6):
            print("Index:", loc + de)
            print("Key Pair:", key_pair[str(loc + de)])

            temp = [r[int(x)] for x in key_pair[str(loc + de)].keys()]
            temp1 = [cipher[int(x)] for x in key_pair[str(loc + de)].values()]

            decrypted_value = decryptor(temp, temp1, r, cipher, Accname, key_pair)
            print("Decrypted Value:", decrypted_value)

            if decrypted_value == message[de]:
                print("Succeeded")
                continue
            else:
                return {"error": "true"}

        return {"error": "false"}

    except Exception as e:
        return {"error": "true"}

