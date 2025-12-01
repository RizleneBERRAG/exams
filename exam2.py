s = input("Saisissez une chaîne : ")

score = 0

for i in range(len(s) - 1):

    val1 = ord(s[i])
    val2 = ord(s[i + 1])

    score += abs(val1 - val2)

print("Score de la chaîne :", score)
