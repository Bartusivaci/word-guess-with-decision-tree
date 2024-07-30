from collections import Counter


def load_wordlist(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return [word.upper() for word in words if '-' not in word and ' ' not in word]

word_list = load_wordlist("wordlist.txt")

def calculate_letter_frequency(possible_words, guesses):
    letter_frequencies = Counter()
    guessed_letter_counts = Counter(guesses)

    for word in possible_words:
        word_letter_counts = Counter(word)
        for letter, count in word_letter_counts.items():
            if count > guessed_letter_counts[letter]:
                letter_frequencies[letter] += 1

    most_common_letter = letter_frequencies.most_common(1)
    if most_common_letter:
        return most_common_letter[0][0]
    else:
        return None


feedback = "--------------------"
guesses = ['E', 'A']
possible_words = []

letter_positions = [index for index, char in enumerate(feedback) if char.isalpha()]
print(letter_positions)

for word in word_list:
    if word in guesses:
        print(f"{word} was guessed")
        continue
    if letter_positions and len(word) < letter_positions[-1] + 1:
        print(f"{word} was too short")
        continue
    match = True
    for guess in guesses:
        if len(guess) == 1 and feedback.count(guess) < guesses.count(guess) and feedback.count(guess) < word.count(guess):
            print(f"{word} has more {guess} letters")
            match = False
            break
    if letter_positions:
        for position in letter_positions:
            if feedback[position] != word[position]:
                print(f"{word} was eliminated")
                match = False
                break
    if match:
        possible_words.append(word)


print(possible_words)
print(calculate_letter_frequency(possible_words, guesses))