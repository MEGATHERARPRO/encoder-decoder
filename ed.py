import random
nl = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
nlr = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
shuffleseed = int(input(" Encoding seed > "))
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
random.seed(shuffleseed)
random.shuffle(el)
random.shuffle(elr)
random.seed(shuffleseed*2)
random.shuffle(el2)
random.shuffle(elr2)
random.seed(shuffleseed*3)
random.shuffle(el3)
random.shuffle(elr3)
random.seed(shuffleseed*4)
random.shuffle(el4)
random.shuffle(elr4)
random.seed(shuffleseed*5)
random.shuffle(el5)
random.shuffle(elr5)
random.seed(shuffleseed*6)
random.shuffle(el6)
random.shuffle(elr6)
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
                elif i1 >= 6:
                    i1 = 0
                    for i in range(length): 
                        if nl[i] == char:
                            em += el6[i]
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
                elif i1 >= 6:
                    i1 = 0
                    for i in range(length2): 
                        if nlr[i] == char:
                            em += elr6[i]
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
                elif i1 >= 6:
                    i1 = 0
                    for i in range(length): 
                        if el6[i] == char:
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
                elif i1 >= 6:
                    i1 = 0
                    for i in range(length2): 
                        if elr6[i] == char:
                            nm += nlr[i]
            else:
                nm += char
        print(" {}".format(nm))
    else:
        print(" Invalid function!")
