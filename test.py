def load_wordlist(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return [word.upper() for word in words]

word_list = load_wordlist("wordlist.txt")


num = 6
possible_word = []

for word in word_list:
    if len(word) == num:
        possible_word.append(word)

print(possible_word)