"""
Word Occurrences counter
Estimate: 15 minutes
Actual:   14:56 minutes
"""


def main():
    string = input("Enter string: ").lower()

    words = string.split()
    words_to_word_occurrences = {}
    for word in words:
        try:
            words_to_word_occurrences[word] += 1
        except KeyError:
            words_to_word_occurrences[word] = 1

    words_number_of_occurrences = list(words_to_word_occurrences.items())
    words_number_of_occurrences.sort()
    width = max(len(words_number_of_occurrence[0]) for words_number_of_occurrence in words_number_of_occurrences)
    for word, count in words_number_of_occurrences:
        print(f"{word:{width}} : {count}")


main()
