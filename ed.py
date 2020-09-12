import random
nl = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
nlr = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
el = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
elr = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
el2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
elr2 = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
el3 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
elr3 = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
el4 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
elr4 = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
el5 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
elr5 = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
el6 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
elr6 = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
el7 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
elr7 = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
el8 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
elr8 = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
el9 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
elr9 = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
el10 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
elr10 = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
el11 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
elr11 = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
el12 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
elr12 = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
el13 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
elr13 = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
el14 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
elr14 = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
el15 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
elr15 = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
el16 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
elr16 = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
el17 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
elr17 = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
el18 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
elr18 = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
el19 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
elr19 = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
el20 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
elr20 = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
el21 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
elr21 = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
el22 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
elr22 = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
el23 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
elr23 = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
el24 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
elr24 = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
el25 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
elr25 = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
ss = str(input(" Encryption key > "))
ssi = 0
print(" Calculating seed 1...")
for char in ss:
    lchar = char.lower()
    if lchar == "a":
        ssi -= 2
    elif lchar == "b":
        ssi -= 4
    elif lchar == "c":
        ssi -= 8
    elif lchar == "d":
        ssi -= 16
    elif lchar == "e":
        ssi -= 32
    elif lchar == "f":
        ssi -= 64
    elif lchar == "g":
        ssi -= 128
    elif lchar == "h":
        ssi -= 256
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
        ssi += 29
    elif lchar == "8":
        ssi += 43
    elif lchar == "9":
        ssi += 61
    elif lchar == "0":
        ssi += 67
    elif lchar == "-":
        ssi += 73
    else:
        ssi -= 512
    ssi ** 4
random.seed(ssi)
random.shuffle(el)
random.shuffle(elr)
print(" Calculating seed 2...")
random.seed(ssi**2)
random.shuffle(el2)
random.shuffle(elr2)
print(" Calculating seed 3...")
random.seed(ssi**3)
random.shuffle(el3)
random.shuffle(elr3)
print(" Calculating seed 4...")
random.seed(ssi**4)
random.shuffle(el4)
random.shuffle(elr4)
print(" Calculating seed 5...")
random.seed(ssi**5)
random.shuffle(el5)
random.shuffle(elr5)
print(" Calculating seed 6...")
random.seed(ssi**6)
random.shuffle(el6)
random.shuffle(elr6)
print(" Calculating seed 7...")
random.seed(ssi**7)
random.shuffle(el7)
random.shuffle(elr7)
print(" Calculating seed 8...")
random.seed(ssi**8)
random.shuffle(el8)
random.shuffle(elr8)
print(" Calculating seed 9...")
random.seed(ssi**9)
random.shuffle(el9)
random.shuffle(elr9)
print(" Calculating seed 10...")
random.seed(ssi**10)
random.shuffle(el10)
random.shuffle(elr10)
print(" Calculating seed 11...")
random.seed(ssi**11)
random.shuffle(el11)
random.shuffle(elr11)
print(" Calculating seed 12...")
random.seed(ssi**12)
random.shuffle(el12)
random.shuffle(elr12)
print(" Calculating seed 13...")
random.seed(ssi**13)
random.shuffle(el13)
random.shuffle(elr13)
print(" Calculating seed 14...")
random.seed(ssi**14)
random.shuffle(el14)
random.shuffle(elr14)
print(" Calculating seed 15...")
random.seed(ssi**15)
random.shuffle(el15)
random.shuffle(elr15)
print(" Calculating seed 16...")
random.seed(ssi**16)
random.shuffle(el16)
random.shuffle(elr16)
print(" Calculating seed 17...")
random.seed(ssi**17)
random.shuffle(el17)
random.shuffle(elr17)
print(" Calculating seed 18...")
random.seed(ssi**18)
random.shuffle(el18)
random.shuffle(elr18)
print(" Calculating seed 19...")
random.seed(ssi**19)
random.shuffle(el19)
random.shuffle(elr19)
print(" Calculating seed 20...")
random.seed(ssi**20)
random.shuffle(el20)
random.shuffle(elr20)
print(" Calculating seed 21...")
random.seed(ssi**21)
random.shuffle(el21)
random.shuffle(elr21)
print(" Calculating seed 22...")
random.seed(ssi**22)
random.shuffle(el22)
random.shuffle(elr22)
print(" Calculating seed 23...")
random.seed(ssi**23)
random.shuffle(el23)
random.shuffle(elr23)
print(" Calculating seed 24...")
random.seed(ssi**24)
random.shuffle(el24)
random.shuffle(elr24)
print(" Calculating seed 25...")
random.seed(ssi**25)
random.shuffle(el25)
random.shuffle(elr25)
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
            if char in nl:
                if i1 == 1:
                    for i in range(length): 
                        if nl[i] == char:
                            em += el[i]
                elif i1 == 2:
                    for i in range(length): 
                        if nl[i] == char:
                            em += el2[i]
                elif i1 == 3:
                    for i in range(length): 
                        if nl[i] == char:
                            em += el3[i]
                elif i1 == 4:
                    for i in range(length): 
                        if nl[i] == char:
                            em += el4[i]
                elif i1 == 5:
                    for i in range(length): 
                        if nl[i] == char:
                            em += el5[i]
                elif i1 == 6:
                    for i in range(length): 
                        if nl[i] == char:
                            em += el6[i]
                elif i1 == 7:
                    for i in range(length): 
                        if nl[i] == char:
                            em += el7[i]
                elif i1 == 8:
                    for i in range(length): 
                        if nl[i] == char:
                            em += el8[i]
                elif i1 == 9:
                    for i in range(length): 
                        if nl[i] == char:
                            em += el9[i]
                elif i1 == 10:
                    for i in range(length): 
                        if nl[i] == char:
                            em += el10[i]
                elif i1 == 11:
                    for i in range(length): 
                        if nl[i] == char:
                            em += el11[i]
                elif i1 == 12:
                    for i in range(length): 
                        if nl[i] == char:
                            em += el12[i]
                elif i1 == 13:
                    for i in range(length): 
                        if nl[i] == char:
                            em += el13[i]
                elif i1 == 14:
                    for i in range(length): 
                        if nl[i] == char:
                            em += el14[i]
                elif i1 == 15:
                    for i in range(length): 
                        if nl[i] == char:
                            em += el15[i]
                elif i1 == 16:
                    for i in range(length): 
                        if nl[i] == char:
                            em += el16[i]
                elif i1 == 17:
                    for i in range(length): 
                        if nl[i] == char:
                            em += el17[i]
                elif i1 == 18:
                    for i in range(length): 
                        if nl[i] == char:
                            em += el18[i]
                elif i1 == 19:
                    for i in range(length): 
                        if nl[i] == char:
                            em += el19[i]
                elif i1 == 20:
                    for i in range(length): 
                        if nl[i] == char:
                            em += el20[i]
                elif i1 == 21:
                    for i in range(length): 
                        if nl[i] == char:
                            em += el21[i]
                elif i1 == 22:
                    for i in range(length): 
                        if nl[i] == char:
                            em += el22[i]
                elif i1 == 23:
                    for i in range(length): 
                        if nl[i] == char:
                            em += el23[i]
                elif i1 == 24:
                    for i in range(length): 
                        if nl[i] == char:
                            em += el24[i]
                elif i1 >= 25:
                    i1 = 0
                    for i in range(length): 
                        if nl[i] == char:
                            em += el25[i]
            elif char in nlr:
                if i1 == 1:
                    for i in range(length2): 
                        if nlr[i] == char:
                            em += elr[i]
                elif i1 == 2:
                    for i in range(length2): 
                        if nlr[i] == char:
                            em += elr2[i]
                elif i1 == 3:
                    for i in range(length2): 
                        if nlr[i] == char:
                            em += elr3[i]
                elif i1 == 4:
                    for i in range(length2): 
                        if nlr[i] == char:
                            em += elr4[i]
                elif i1 == 5:
                    for i in range(length2): 
                        if nlr[i] == char:
                            em += elr5[i]
                elif i1 == 6:
                    for i in range(length2): 
                        if nlr[i] == char:
                            em += elr6[i]
                elif i1 == 7:
                    for i in range(length2): 
                        if nlr[i] == char:
                            em += elr7[i]
                elif i1 == 8:
                    for i in range(length2): 
                        if nlr[i] == char:
                            em += elr8[i]
                elif i1 == 9:
                    for i in range(length): 
                        if nlr[i] == char:
                            em += elr9[i]
                elif i1 == 10:
                    for i in range(length): 
                        if nlr[i] == char:
                            em += elr10[i]
                elif i1 == 11:
                    for i in range(length): 
                        if nlr[i] == char:
                            em += elr11[i]
                elif i1 == 12:
                    for i in range(length): 
                        if nlr[i] == char:
                            em += elr12[i]
                elif i1 == 13:
                    for i in range(length): 
                        if nlr[i] == char:
                            em += elr13[i]
                elif i1 == 14:
                    for i in range(length): 
                        if nlr[i] == char:
                            em += elr14[i]
                elif i1 == 15:
                    for i in range(length): 
                        if nlr[i] == char:
                            em += elr15[i]
                elif i1 == 16:
                    for i in range(length): 
                        if nlr[i] == char:
                            em += elr16[i]
                elif i1 == 17:
                    for i in range(length): 
                        if nlr[i] == char:
                            em += elr17[i]
                elif i1 == 18:
                    for i in range(length): 
                        if nlr[i] == char:
                            em += elr18[i]
                elif i1 == 19:
                    for i in range(length): 
                        if nlr[i] == char:
                            em += elr19[i]
                elif i1 == 20:
                    for i in range(length): 
                        if nlr[i] == char:
                            em += elr20[i]
                elif i1 == 21:
                    for i in range(length): 
                        if nlr[i] == char:
                            em += elr21[i]
                elif i1 == 22:
                    for i in range(length): 
                        if nlr[i] == char:
                            em += elr22[i]
                elif i1 == 23:
                    for i in range(length): 
                        if nlr[i] == char:
                            em += elr23[i]
                elif i1 == 24:
                    for i in range(length): 
                        if nlr[i] == char:
                            em += elr24[i]
                elif i1 >= 25:
                    i1 = 0
                    for i in range(length): 
                        if nlr[i] == char:
                            em += elr25[i]
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
            if char in nl:
                if i1 == 1:
                    for i in range(length): 
                        if el[i] == char:
                            nm += nl[i]
                elif i1 == 2:
                    for i in range(length): 
                        if el2[i] == char:
                            nm += nl[i]
                elif i1 == 3:
                    for i in range(length): 
                        if el3[i] == char:
                            nm += nl[i]
                elif i1 == 4:
                    for i in range(length): 
                        if el4[i] == char:
                            nm += nl[i]
                elif i1 == 5:
                    for i in range(length): 
                        if el5[i] == char:
                            nm += nl[i]
                elif i1 == 6:
                    for i in range(length): 
                        if el6[i] == char:
                            nm += nl[i]
                elif i1 == 7:
                    for i in range(length): 
                        if el7[i] == char:
                            nm += nl[i]
                elif i1 == 8:
                    for i in range(length): 
                        if el8[i] == char:
                            nm += nl[i]
                elif i1 == 9:
                    for i in range(length): 
                        if el9[i] == char:
                            nm += nl[i]
                elif i1 == 10:
                    for i in range(length): 
                        if el10[i] == char:
                            nm += nl[i]
                elif i1 == 10:
                    for i in range(length): 
                        if el10[i] == char:
                            nm += nl[i]
                elif i1 == 11:
                    for i in range(length): 
                        if el11[i] == char:
                            nm += nl[i]
                elif i1 == 12:
                    for i in range(length): 
                        if el12[i] == char:
                            nm += nl[i]
                elif i1 == 13:
                    for i in range(length): 
                        if el13[i] == char:
                            nm += nl[i]
                elif i1 == 14:
                    for i in range(length): 
                        if el14[i] == char:
                            nm += nl[i]
                elif i1 == 15:
                    for i in range(length): 
                        if el15[i] == char:
                            nm += nl[i]
                elif i1 == 16:
                    for i in range(length): 
                        if el16[i] == char:
                            nm += nl[i]
                elif i1 == 17:
                    for i in range(length): 
                        if el17[i] == char:
                            nm += nl[i]
                elif i1 == 18:
                    for i in range(length): 
                        if el18[i] == char:
                            nm += nl[i]
                elif i1 == 19:
                    for i in range(length): 
                        if el19[i] == char:
                            nm += nl[i]
                elif i1 == 20:
                    for i in range(length): 
                        if el20[i] == char:
                            nm += nl[i]
                elif i1 == 21:
                    for i in range(length): 
                        if el21[i] == char:
                            nm += nl[i]
                elif i1 == 22:
                    for i in range(length): 
                        if el22[i] == char:
                            nm += nl[i]
                elif i1 == 23:
                    for i in range(length): 
                        if el23[i] == char:
                            nm += nl[i]
                elif i1 == 24:
                    for i in range(length): 
                        if el24[i] == char:
                            nm += nl[i]
                elif i1 >= 25:
                    i1 = 0
                    for i in range(length): 
                        if el25[i] == char:
                            nm += nl[i]
            elif char in nlr:
                if i1 == 1:
                    for i in range(length2): 
                        if elr[i] == char:
                            nm += nlr[i]
                elif i1 == 2:
                    for i in range(length2): 
                        if elr2[i] == char:
                            nm += nlr[i]
                elif i1 == 3:
                    for i in range(length2): 
                        if elr3[i] == char:
                            nm += nlr[i]
                elif i1 == 4:
                    for i in range(length2): 
                        if elr4[i] == char:
                            nm += nlr[i]
                elif i1 == 5:
                    for i in range(length2): 
                        if elr5[i] == char:
                            nm += nlr[i]
                elif i1 == 6:
                    for i in range(length2): 
                        if elr6[i] == char:
                            nm += nlr[i]
                elif i1 == 7:
                    for i in range(length2): 
                        if elr7[i] == char:
                            nm += nlr[i]
                elif i1 == 8:
                    for i in range(length2): 
                        if elr8[i] == char:
                            nm += nlr[i]
                elif i1 == 9:
                    for i in range(length): 
                        if elr9[i] == char:
                            nm += nlr[i]
                elif i1 == 10:
                    for i in range(length): 
                        if elr10[i] == char:
                            nm += nlr[i]
                elif i1 == 10:
                    for i in range(length): 
                        if elr10[i] == char:
                            nm += nlr[i]
                elif i1 == 11:
                    for i in range(length): 
                        if elr11[i] == char:
                            nm += nlr[i]
                elif i1 == 12:
                    for i in range(length): 
                        if elr12[i] == char:
                            nm += nlr[i]
                elif i1 == 13:
                    for i in range(length): 
                        if elr13[i] == char:
                            nm += nlr[i]
                elif i1 == 14:
                    for i in range(length): 
                        if elr14[i] == char:
                            nm += nlr[i]
                elif i1 == 15:
                    for i in range(length): 
                        if elr15[i] == char:
                            nm += nlr[i]
                elif i1 == 16:
                    for i in range(length): 
                        if elr16[i] == char:
                            nm += nlr[i]
                elif i1 == 17:
                    for i in range(length): 
                        if elr17[i] == char:
                            nm += nlr[i]
                elif i1 == 18:
                    for i in range(length): 
                        if elr18[i] == char:
                            nm += nlr[i]
                elif i1 == 19:
                    for i in range(length): 
                        if elr19[i] == char:
                            nm += nlr[i]
                elif i1 == 20:
                    for i in range(length): 
                        if elr20[i] == char:
                            nm += nlr[i]
                elif i1 == 21:
                    for i in range(length): 
                        if elr21[i] == char:
                            nm += nlr[i]
                elif i1 == 22:
                    for i in range(length): 
                        if elr22[i] == char:
                            nm += nlr[i]
                elif i1 == 23:
                    for i in range(length): 
                        if elr23[i] == char:
                            nm += nlr[i]
                elif i1 == 24:
                    for i in range(length): 
                        if elr24[i] == char:
                            nm += nlr[i]
                elif i1 >= 25:
                    i1 = 0
                    for i in range(length): 
                        if elr25[i] == char:
                            nm += nlr[i]
            else:
                nm += char
        print(" {}".format(nm))
    else:
        print(" Invalid function!")
