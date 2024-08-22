"""
    To use this implementation, you simply have to implement `agent_function` such that it returns a legal action.
    You can then let your agent compete on the server by calling
        python3 advanced.py path/to/your/config.json

    You can interrupt the script at any time.
    The server will remember the actions you have sent.

    Note:
        By default the client bundles multiple requests for efficiency.
        This can complicate debugging.
        You can disable it by setting `parallel_runs=False` in the last line.
"""
from collections import Counter


def load_wordlist(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return [word.upper() for word in words if
            '-' not in word and ' ' not in word and '±' not in word and 'Ã' not in word]


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


def agent_function(request_data, request_info):
    # TODO: Implement this function in a better way.
    # The request_data contains all the relevant information (map, history, ...).
    # You can ignore request_info.
    print('I got the following request:')
    print(request_data)

    word_list = load_wordlist("wordlist.txt")

    feedback = request_data["feedback"]
    guesses = request_data["guesses"]

    possible_words = []

    letter_positions = [index for index, char in enumerate(feedback) if char.isalpha()]

    for word in word_list:
        if word in guesses:
            continue
        if letter_positions and len(word) < letter_positions[-1] + 1:
            continue
        match = True
        for guess in guesses:
            if len(guess) == 1 and feedback.count(guess) < guesses.count(guess) and feedback.count(guess) < word.count(
                    guess):
                match = False
                break
        if letter_positions:
            for position in letter_positions:
                if feedback[position] != word[position]:
                    match = False
                    break
        if match:
            possible_words.append(word)

    if len(possible_words) < 4:
        return possible_words[0]
    elif len(possible_words) < 30 and 'X' not in guesses:
        contains_x = any('X' in word for word in possible_words)
        if contains_x:
            x_words = [word for word in possible_words if 'X' in word]
            if len(x_words) < 6:
                return x_words[0]
            else:
                most_frequent_letter = calculate_letter_frequency(x_words, guesses)
                return most_frequent_letter
        else:
            most_frequent_letter = calculate_letter_frequency(possible_words, guesses)
            return most_frequent_letter
    else:
        most_frequent_letter = calculate_letter_frequency(possible_words, guesses)
        return most_frequent_letter



if __name__ == '__main__':
    import sys, logging
    from client import run

    # You can set the logging level to logging.WARNING or logging.ERROR for less output.
    logging.basicConfig(level=logging.INFO)

    run(
        agent_function=agent_function,
        agent_config_file=sys.argv[1],
        parallel_runs=True,  # Set it to False for debugging.
        run_limit=1000,  # Stop after 1000 runs. Set to 1 for debugging.
    )

