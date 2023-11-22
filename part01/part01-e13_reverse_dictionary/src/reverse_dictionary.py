#!/usr/bin/env python3

def reverse_dictionary(d: dict) -> dict:
    """Reverse the keys and values in the dictionary
    and a dictionary and return a new dictionary.
    """
    finnish_words = set([w for word in d.values() for w in word])
    english_dict = {word: [] for word in finnish_words}
    for finnish_word in finnish_words:
        for english_word, finnish_translation in d.items():
            if finnish_word in finnish_translation:
                english_dict[finnish_word].append(english_word)
    return english_dict


def main() -> None:
    d = {
        'move': ['liikuttaa'],
        'hide': ['piilottaa', 'salata'],
        'six': ['kuusi'],
        'fir': ['kuusi']
    }
    print(reverse_dictionary(d))


if __name__ == "__main__":
    main()
