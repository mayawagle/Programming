password = "kFyf;haH3rsV"

# passwordEasy = "k"

# for s in range(33, 127):
#     print(s,chr(s))
#     if chr(s) == passwordEasy:
#         print('you got the password! It is', chr(s))
#         break

passwordMedium = "kF"
myPasswordGuess = ""
flag = False

for s in range(33, 127):
    print(s,chr(s))
    # myPasswordGuess = chr(s)
    for t in range(33, 127):
        myPasswordGuess = chr(s) + chr(t)
        print(chr(s) + chr(t))
        if myPasswordGuess == passwordMedium:
            print('you got the password! It is', myPasswordGuess)
            flag = True
            break
    if flag == True:
        break

