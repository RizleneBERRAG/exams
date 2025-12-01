s = input("Saisir une phrase : ")

s = s.strip()

last_word_length = 0
current_length = 0

for char in s:
    if char != " ":
        current_length += 1
        last_word_length = current_length
    else:
        current_length = 0

print("Longueur du dernier mot :", last_word_length)
