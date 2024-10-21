import hashlib

ghg = "s"
currenthash = "sha256"
tripname = [""]
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
x = " ".join(tripname)
pepperonicounter = [x]

if pepperonicounter[0] == " ".join(tripname):
    pepperoniboy = True
    for letter in ghg:
        alphjoin = (x, alphabet[3] + alphabet[8] + alphabet[4])
        thealphbetjoined = " ".join(alphjoin)
        sha256 = hashlib.sha256()
        sha256.update(thealphbetjoined.encode('utf-8'))
        string_hash = sha256.hexdigest()
        pepperonicounter.append(thealphbetjoined)

        print(f"Hashed message in {currenthash}")
        print("Hashed: "+string_hash)
        print("Dehashed:"+pepperonicounter[1])
