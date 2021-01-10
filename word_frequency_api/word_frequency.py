"""Word frequency class."""

import collections


class WordFrequency:
    """Class WordFrequency."""

    def __init__(self, text: str = "", word: str = "") -> None:
        self.text = text.lower()
        self.word = word.lower()

    def calculate_highest_frequency(self) -> list:
        """Calculate highest frequency of word in a text.

        Returns:
            List of higher frequency of word(s).
        """
        counts = collections.Counter(self.text.split())
        number_max_occurence = counts.most_common()[0][1]
        return [
            word_frequency
            for word_frequency in counts.most_common()
            if word_frequency[1] == number_max_occurence
        ]

    def calculate_frequency_for_word(self) -> int:
        """Calculate the frequency of a word in a text.

        Returns:
            Number a word frequency in the text.
        """
        return self.text.count(self.word)

    def calculate_most_frequent_words(self) -> list:
        """Calculate the most occurrence of word in a text.

        Returns:
            List of higher frequency of word(s).
        """
        counts = collections.Counter(self.text.split())
        all_frequencies = counts.most_common()
        return sorted(all_frequencies, key=lambda element: (-element[1], element[0]))
