import random
nl = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
nlr = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
ss = str(input(" Encryption key > "))
ssi = 0
for char in ss:
    lchar = char.lower()
    elif lchar == "1":
        ssi += 3
    elif lchar == "2":
        ssi += 5
    elif lchar == "3":
        ssi += 7
    elif lchar == "4":
        ssi += 11
    elif lchar == "5":
        ssi += 13
    elif lchar == "6":
        ssi += 17
    elif lchar == "7":
        ssi += 19
    elif lchar == "8":
        ssi += 23
    elif lchar == "9":
        ssi += 29
    elif lchar == "0":
        ssi += 31
    elif lchar == "-":
        ssi += 37
    elif lchar == "!":
        ssi += 43
    elif lchar == "@":
        ssi += 47
    elif lchar == "#":
        ssi += 53
    if lchar in "a":
        ssi += 61
    elif lchar in "b":
        ssi += 67
    elif lchar in "c":
        ssi += 71
    elif lchar in "d":
        ssi += 73
    elif lchar in "e":
        ssi += 79
    elif lchar in "f":
        ssi += 83
    elif lchar in "g":
        ssi += 89
    elif lchar in "h":
        ssi += 97
    elif lchar in "i":
        ssi += 101
    elif lchar in "j":
        ssi += 103
    elif lchar in "k":
        ssi += 107
    elif lchar in "l":
        ssi += 109
    elif lchar in "m":
        ssi += 113
    elif lchar in "n":
        ssi += 127
    elif lchar in "o":
        ssi += 131
    elif lchar in "p":
        ssi += 137
    elif lchar in "q":
        ssi += 139
    elif lchar in "r":
        ssi += 149
    elif lchar in "s":
        ssi += 151
    else:
        ssi += 59
    ssi ** 4
userinput1 = ""
length = len(nl)
length2 = len(nlr)
while userinput1 != "exit":
    userinput1 = str(input(" Do you want to decode or encode? (E/D) "))
    if userinput1.lower() == "e" or userinput1.lower() == "encode":
        userinput2 = str(input(" > "))
        i1 = 0
        nm = userinput2.lower()
        em = ""
        for char in nm:
            i1 += 1
            el = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
            elr = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
            cssi = ssi + ssi * i1
            random.seed(cssi)
            random.shuffle(el)
            random.seed(cssi)
            random.shuffle(elr)
            if char in nl:
                for i in range(length): 
                    if nl[i] == char:
                        em += el[i]
            elif char in nlr:
                for i in range(length): 
                    if nlr[i] == char:
                        em += elr[i]
            else:
                em += char
        print(" {}".format(em))
    elif userinput1.lower() == "d" or userinput1.lower() == "decode":
        userinput2 = str(input(" > "))
        i1 = 0
        nm = ""
        em = userinput2.lower()
        for char in em:
            i1 += 1
            el = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
            elr = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
            cssi = ssi + ssi * i1
            random.seed(cssi)
            random.shuffle(el)
            random.seed(cssi)
            random.shuffle(elr)
            if char in nl:
                for i in range(length): 
                    if el[i] == char:
                        nm += nl[i]
            elif char in nlr:
                for i in range(length): 
                    if elr[i] == char:
                        nm += nlr[i]
            else:
                nm += char
        print(" {}".format(nm))
    else:
        print(" Invalid function!")
