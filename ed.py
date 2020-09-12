import random
nl = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y","z", "а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
random.shuffle(nl)
print(nl)
userinput1 = ""
length = len(nl)
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
            else:
                nm += char
        print(" {}".format(nm))
    else:
        print(" Invalid function!")
