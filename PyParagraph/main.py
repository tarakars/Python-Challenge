import os
import re

paragraph_path = os.path.join("raw_data", "paragraph_2.txt")


with open(paragraph_path,'r') as text:
    paragraph = text.read()
    words = paragraph.split(" ")
    word_count = len(words)
    print(str(word_count))
    sentence = paragraph.split(".")
    sentence_count = len(sentence)
    print(str(sentence_count))
    average_sentence_length = (word_count/sentence_count)
    print(average_sentence_length)
    letters = list(paragraph)
    average_letter_count = (len(letters)/word_count)
    print(average_letter_count)



