"""Input module"""

from word_frequency_api.word_frequency import WordFrequency

text = ""
word = ""

obj = WordFrequency(text=text, word=word)

print(obj.calculate_highest_frequency())
print(obj.calculate_frequency_for_word())
print(obj.calculate_most_frequent_words())
